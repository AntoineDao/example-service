#!/bin/sh
NEW_VERSION = $0
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build . -t $TRAVIS_REPO_SLUG:NEW_VERSION 
docker push $TRAVIS_REPO_SLUG:NEW_VERSION 
docker push $TRAVIS_REPO_SLUG

curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl

IFS=/ read ORG REPOSITORY <<< $TRAVIS_REPO_SLUG
sed -i "s/{{COMMIT_TAG}}/NEW_VERSION/g" service.yml
sed -i "s/{{ORG}}/$ORG/g" service.yml
sed -i "s/{{REPOSITORY}}/$REPOSITORY/g" service.yml
sed -i "s/{{NAMESPACE}}/$NAMESPACE/g" service.yml
sed -i "s/{{ENDPOINT}}/$ENDPOINT/g" service.yml


kubectl --kubeconfig=kubeconfig apply -f service.yml