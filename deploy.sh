#!/bin/sh
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build . -t $TRAVIS_REPO_SLUG:$COMMIT_TAG 
docker push $TRAVIS_REPO_SLUG:$COMMIT_TAG 
docker push $TRAVIS_REPO_SLUG:latest

curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl

IFS=/ read ORG REPOSITORY <<< $TRAVIS_REPO_SLUG
sed -i "s/COMMIT_TAG/$COMMIT_TAG/g" service.yml
sed -i "s/TRAVIS_REPO_SLUG/$TRAVIS_REPO_SLUG/g" service.yml
sed -i "s/REPOSITORY/$REPOSITORY/g" service.yml


kubectl --kubeconfig=kubeconfig apply -f service.yml