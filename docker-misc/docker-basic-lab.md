## Create a docker file

#### Dockerfile
```dockerfile
FROM nginx:alpine

RUN touch /usr/share/nginx/html/index.html && echo "Hello Nginx" > /usr/share/nginx/html/index.html

```

#### Build and run the image
```bash
docker build -t hello-nginx .
docker run --rm -d -p 8000:80 hello-nginx
docker run -d -p 8000:80 hello-nginx
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
docker rmi hello-nginx

# Prune the Docker system
# These commands are dangerous and should be used with caution
docker container prune -f # This will remove all the containers
docker volume prune -f # This will remove all the volumes
docker network prune -f # This will remove all the networks
docker system prune -a -f # This will remove all the containers, images, networks, and volumes
```
