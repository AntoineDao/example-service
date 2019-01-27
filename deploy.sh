#!/bin/sh
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build . -t $TRAVIS_REPO_SLUG:$COMMIT 
docker push $TRAVIS_REPO_SLUG:$COMMIT 

curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl

sed -i 's/COMMIT_TAG/$COMMIT/g' service.yml

kubectl --kubeconfig=kubeconfig apply -f service.yml