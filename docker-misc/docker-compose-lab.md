# Docker Lab


### Laravel Project Structure:
```
laravel_project/
├── app/
├── bootstrap/
├── config/
├── ...
└── devops/
    └── docker/
        ├── nginx.conf
        ├── php.dockerfile
        ├── entrypoint.sh
        ├── www.conf
|── ...
|── .env
|── .env.example
|── ...
|── docker-compose.yml
```


### devops/docker/www.conf
```ini
[www]

user = www-data
group = www-data

listen = 127.0.0.1:9000

pm = dynamic

pm.max_children = 5
pm.start_servers = 2
pm.min_spare_servers = 1
pm.max_spare_servers = 3

```

### devops/docker/php.dockerfile
```dockerfile
# Use a PHP image with PHP-FPM
FROM php:8.1-fpm-alpine

# Install additional PHP extensions and dependencies
RUN apk add --no-cache \
    libzip-dev \
    zip \
    unzip \
    nodejs \
    npm \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install zip \
    && docker-php-ext-install bcmath \
    && docker-php-ext-install pcntl 

# Copy the PHP-FPM configuration file
ADD devops/docker/www.conf /usr/local/etc/php-fpm.d/www.conf


# Set the working directory
RUN mkdir -p /var/www/html && chown www-data:www-data /var/www/html
WORKDIR /var/www/html


# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

```

### devops/docker/nginx.conf
```nginx
server {
    listen 80;
    index index.php index.html;
    server_name localhost;
    root /var/www/html/public;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        try_files $uri = 404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass kt_php:9000;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
    }
}

```

### .env
```ini
DB_CONNECTION=mysql
DB_HOST=kt_mysql
DB_PORT=3306
DB_DATABASE=kt_laravel_db
DB_USERNAME=kt_laravel_user
DB_PASSWORD=kt_laravel_password

```

### docker-compose.yml:\
```yaml
version: '3'

services:
  kt_mysql:
    image: mysql:latest
    container_name: kt_mysql
    environment:
      MYSQL_ROOT_PASSWORD: root_password
      MYSQL_DATABASE: kt_laravel_db
      MYSQL_USER: kt_laravel_user
      MYSQL_PASSWORD: kt_laravel_password
    volumes:
      - kt_mysql_volume:/var/lib/mysql
    networks:
      - kt_network

  kt_php:
    build:
      dockerfile: devops/docker/php.dockerfile
    container_name: kt_php
    volumes:
      - ./:/var/www/html
    depends_on:
      - kt_mysql
    networks:
      - kt_network
      
  kt_nginx:
    image: nginx:latest
    container_name: kt_nginx
    ports:
      - "8080:80"
    volumes:
      - ./:/var/www/html
      - ./devops/docker/nginx.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - kt_php
    networks:
      - kt_network

networks:
  kt_network:
    driver: bridge

volumes:
  kt_mysql_volume:


```

## Docker Commands:
```bash
# Build the Docker containers
docker-compose build
docker-compose up -d
docker-compose exec kt_php composer install
docker-compose exec kt_php php artisan key:generate
docker-compose exec kt_php php artisan migrate
docker-compose exec kt_php php artisan db:seed
docker-compose exec kt_php npm install
docker-compose exec kt_php npm run build
docker exec -it kt_php php sh
docker-compose down
```

