# Example Service

This repository serves as an example of how to configure a microservice repository for deployment to the pollination kubernetes cluster. 

## Continuous Deployment
Configuring continuous deployment is done by running the `deploy.sh` script in the root of the repository. This script requires the following environment variables to be set in the `.travis.yml` file:
* COMMIT_TAG: an 8 character version of the commit sha
* NAMSEPACE: the namespace in the kubernetes cluster the service will be deployed to
* ENDPOINT: the url endpoint the service will be accessible from eg: `example` for `api.pollination.cloud/example`
* DOCKER_USERNAME: the username of the docker user pushing the image to the pollination registry
* DOCKER_PASSWORD: the password of the docker user pushing the image to the pollination registry

The initial `.travis.yml` file looks like this:
```yaml
services:
- docker
language: python
python:
- '3.6'
jobs:
  include:
  - stage: deploy
    if: branch = master AND (NOT type IN (pull_request))
    provider: script
    script: bash deploy.sh
```

The Docker credentials are encrypt into the travis file by using the [travis cli](https://github.com/travis-ci/travis.rb):
> travis encrypt DOCKER_USERNAME=whaleymacwhale --add

> travis encrypt DOCKER_password=idontlikeishmael --add

We also encrypt a kubeconfig file that will be used by kubectl to deploy the changes to the pollination cluster. The kubeconfig file can be encrypted as follows:
> travis encrypt-file PATH_TO_KUBECONFIG_FILE --add