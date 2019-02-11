import os
import boto3

region_name = os.getenv('BUCKET_REGION', 'sfo2')
endpoint_url = os.getenv('BUCKET_URL', 'https://sfo2.digitaloceanspaces.com')
aws_access_key_id = os.getenv('BUCKET_ACCESS_KEY')
aws_secret_access_key = os.getenv('BUCKET_SECRET_ACCESS_KEY')
bucket_name = os.getenv('BUCKET_NAME', 'pollination')
bucket_url_expiration = int(os.getenv('BUCKET_URL_EXPIRATION', '3600'))

session = boto3.session.Session()
client = session.client('s3',
                        region_name=region_name,
                        endpoint_url=endpoint_url,
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key)


def get_upload_url(user_id, file_name, bucket=bucket_name):
    key = 'users/{user_id}/uploads/{file_name}'.format(user_id=user_id, file_name=file_name)
    url = client.generate_presigned_url('put_object',
                                        Params={'Bucket': bucket, 'Key':key},
                                        ExpiresIn=bucket_url_expiration,
                                        HttpMethod='PUT')
    return url

def list_files(user_id, bucket=bucket_name):
    prefix = 'users/{}/uploads/'.format(user_id)
    response = client.list_objects(Bucket=bucket, Prefix=prefix)
    if response.get('ResponseMetadata').get('HTTPStatusCode') == 200:
        contents = response.get('Contents')
        if contents is not None:
            files = [content['Key'] for content in contents]
        else:
            files = []
        return files
    else:
        print(response) # log error to be captured through stdout logging system
        raise Exception('Something went wrong when fetching data from buckets')