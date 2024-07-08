#!/bin/bash

echo -e "\n\nStopping all running Docker containers..."
docker stop $(docker ps -q)

echo -e "\n\nRemoving all Docker containers..."
docker rm $(docker ps -aq)

echo -e "\n\nRemoving all Docker images..."
docker rmi -f $(docker images -q)

echo -e "\n\nBuilding Docker image..."
docker build -t nutriinsights-be ./be

echo -e "\n\nTagging Docker image..."
docker tag nutriinsights-be:latest 590183905213.dkr.ecr.ap-northeast-2.amazonaws.com/nutriinsights-be:latest

echo -e "\n\nLogging in to AWS ECR..."
/mnt/c/Program\ Files/Amazon/AWSCLIV2/aws.exe ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 590183905213.dkr.ecr.ap-northeast-2.amazonaws.com

echo -e "\n\nPushing Docker image to ECR..."
docker push 590183905213.dkr.ecr.ap-northeast-2.amazonaws.com/nutriinsights-be:latest