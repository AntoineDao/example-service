from flask_restplus import fields

example = {
    'id': fields.String(),
    'email': fields.String(required=True, error_message='email is required'),
    'username': fields.String(required=True, error_message='username is required'),
    'password': fields.String(required=True, load_only=True, error_message='password is required')
}
