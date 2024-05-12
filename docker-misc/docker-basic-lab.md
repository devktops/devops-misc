## Create a docker file

#### Dockerfile
```dockerfile
# Use Alpine Linux as base image
FROM alpine:latest

# Install nginx
RUN apk update && \
    apk add nginx && \
    rm -rf /var/cache/apk/*

# Copy nginx configuration file
COPY nginx.conf /etc/nginx/http.d/default.conf

# Create html directory
RUN mkdir -p /var/www/html

# Copy index.html to /var/www/html
COPY index.html /var/www/html/

# Change ownership of /var/www/html to user 'nginx'
RUN chown -R nginx:nginx /var/www/html

# Set working directory
WORKDIR /var/www/html

# Expose port 80
EXPOSE 80

# Start nginx on container startup
CMD ["nginx", "-g", "daemon off;"]

```

#### nginx.conf
```nginx
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;

        index index.html index.html;
        

        # Everything is a 404
        location / {
                try_files $uri $uri/ =404;
        }

        # You may need this to prevent return 404 recursion.
        location = /404.html {
                internal;
        }
}
```

#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to DevKTOps</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <div class="jumbotron mt-5">
            <h1 class="display-4">Welcome to DevKTOps!</h1>
            <p class="lead">This is a simple web page served by nginx inside a Docker container.</p>
            <hr class="my-4">
            <p>Empowering your DevOps journey.</p>
        </div>
    </div>
    <!-- Bootstrap JS -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

#### Build and run the image
```bash
docker build -t hello-kt .

# run the container in the background and map port 8000 on the host to port 80 on the container
docker run --rm -d -p 8000:80 hello-kt
docker run -d -p 8000:80 hello-kt
```

#### Pushing the image to Docker Hub
```bash
# Tag the image
docker tag hello-kt thixpin/hello-kt

# Tag the image with a version
docker tag hello-kt thixpin/hello-kt:1.0

# Docker login
docker login

# Push the image to Docker Hub
docker push thixpin/hello-kt
docker push thixpin/hello-kt:1.0
```


### Docker Volume and Network

#### Commands to create a volume and network
```bash
# Create a Docker volume
docker volume create my-vol

# List the Docker volumes
docker volume ls

# Create a Docker network
docker network create my-net

# List the Docker networks
docker network ls


# Run the containers with the volume and network
docker run -d --name c1 --network my-net -v my-vol:/usr/share/nginx/html -p 8001:80 nginx:alpine
docker run -d --name c2 --network my-net -v my-vol:/usr/share/nginx/html nginx:alpine

# Add a file to the volume
docker exec -it c1 sh
cd /usr/share/nginx/html
ls
touch hello.html
echo "Hello World" > hello.html
ls

# Check the volume
docker exec c1 ls /usr/share/nginx/html
docker exec c1 ls /usr/share/nginx/html

# List the containers
docker ps -a

# Inspect the Docker volume
docker volume inspect my-vol


# Inspect the Docker network
docker network inspect my-net

# Very connectivty between the containers
docker exec c1 ping c2
docker exec c2 ping c1

# Remove the containers
docker rm -f c1 c2


# Remove the volume
docker volume rm my-vol

# Remove the network
docker network rm my-net

# remove the image
docker rmi hello-kt

# Prune the Docker system
# These commands are dangerous and should be used with caution
docker container prune -f # This will remove all the containers
docker volume prune -f # This will remove all the volumes
docker network prune -f # This will remove all the networks
docker system prune -a -f # This will remove all the containers, images, networks, and volumes
```
