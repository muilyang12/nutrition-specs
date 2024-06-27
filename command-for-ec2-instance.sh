echo -e "\n\nLogging in to AWS ECR..."
docker stop $(docker ps -q) && docker rm $(docker ps -aq) && docker rmi $(docker images -q)

echo -e "\n\nPulling Docker image from ECR..."
docker pull 590183905213.dkr.ecr.ap-northeast-2.amazonaws.com/nutrition-comparison-be:latest

echo -e "\n\nStarting Docker container..."
docker run -d --name backend -p 80:80 --restart always 590183905213.dkr.ecr.ap-northeast-2.amazonaws.com/nutrition-comparison-be:latest && docker ps -a