
# Deploying a Next.js Application on AWS ECS

## Prerequisites

1. **AWS Account**: Ensure you have an AWS account.
2. **AWS CLI**: Install and configure the AWS CLI.
3. **Docker**: Install Docker to build the Docker image of your Next.js application.
4. **AWS IAM User**: Ensure you have an IAM user with the necessary permissions to create and manage AWS resources.

## Steps

### 1. Set Up Next.js Application

First, let's clone the simple Next.js application from GitHub:


```bash
git clone https://github.com/devktops/nextjs-app.git my-nextjs-app
cd my-nextjs-app
```

### 2. Dockerize Next.js Application

Create a `Dockerfile` in the root of your Next.js project:

```dockerfile

FROM node:18-alpine

LABEL maintainer="Soe Thura <thixpin@gmail.com>"
LABEL description="Docker image for Next.js app"

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Build the Next.js application
RUN npm run build

# Expose the port Next.js app runs on
EXPOSE 3000

# Define the command to run the app
CMD ["npm", "run", "start", "-p", "3000"]
```

Build the Docker image:

```bash
export AWS_REGION=ap-southeast-1
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
export APP_NAME=my-nextjs-app
echo $AWS_ACCOUNT_ID

docker build -t $APP_NAME .
```

### 3. Push Docker Image to Amazon ECR

1. **Create ECR Repository**:

```bash
aws ecr create-repository --repository-name $APP_NAME
```

2. **Authenticate Docker to ECR**:

```bash
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
```

3. **Tag and Push Image to ECR**:

```bash
docker tag $APP_NAME:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$APP_NAME:latest
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$APP_NAME:latest

echo "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$APP_NAME:latest",
```

### 4. Set Up ECS Cluster

1. **Create ECS Cluster**:

```bash
aws ecs create-cluster --cluster-name my-nextjs-cluster
```

2. **Create Task Definition**:

Create a JSON file (`task-definition.json`) with the following command:


```bash
cat > task-definition.json << EOF
{
  "family": "my-nextjs-task",
  "networkMode": "awsvpc",
  "containerDefinitions": [
    {
      "name": "my-nextjs-container",
      "image": "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$APP_NAME:latest",
      "memory": 512,
      "cpu": 256,
      "portMappings": [
        {
          "containerPort": 3000,
          "hostPort": 3000,
          "protocol": "tcp"
        }
      ]
    }
  ],
  "requiresCompatibilities": [
    "FARGATE"
  ],
  "cpu": "256",
  "memory": "512"
}
EOF
```

Register the task definition:

```bash
aws ecs register-task-definition --cli-input-json file://task-definition.json
```

3. **Create ECS Service**:

```bash
aws ecs create-service --cluster my-nextjs-cluster --service-name my-nextjs-service --task-definition my-nextjs-task --desired-count 1 --launch-type FARGATE --network-configuration "awsvpcConfiguration={subnets=[<your-subnet-id>],securityGroups=[<your-security-group-id>],assignPublicIp=ENABLED}" --load-balancers targetGroupArn=<your-target-group-arn>,containerName=my-nextjs-container,containerPort=3000
```

Replace `<your-subnet-id>`, `<your-security-group-id>`  and `<your-target-group-arn>` with the appropriate values.

### 5. Accessing the Application

Once the ECS service is up and running, you can access your Next.js application using the public IP address assigned to the Fargate task. You can find this IP address in the ECS console under the Tasks tab for your service.

## Conclusion

By following these steps, you will have successfully deployed a Next.js application on AWS ECS using Fargate. This setup provides a scalable and managed environment for running your web applications.

For more advanced configurations and optimizations, you can explore additional features of ECS, such as load balancing, auto-scaling, and monitoring.