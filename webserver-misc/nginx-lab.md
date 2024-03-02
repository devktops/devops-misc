# Installing Nginx on Ubuntu and creating a virtual host

## Installing Nginx
Some operating systems come with apache2 installed by default. If you want to install Nginx, you need to remove apache2 first. You can do this by running the following commands:

```bash
sudo systemctl stop apache2
sudo systemctl disable apache2
sudo apt remove apache2
```

Then you can install Nginx by running the following commands:

```bash
sudo apt update
sudo apt install nginx
sudo systemctl enable --now nginx
sudo systemctl status nginx
```

## Creating a virtual host
You can create a virtual host by creating a new configuration file in the `/etc/nginx/sites-available` directory. For example, you can create a file called `example.com` by running the following command:

```bash
sudo nano /etc/nginx/sites-available/example.com
```

Then you can add the following configuration to the file:

```nginx
server {
    listen 80;
    server_name example.com www.example.com;
    root /var/www/example.com;
    index index.html;
}
```

After creating the configuration file, you need to create a symbolic link to the `/etc/nginx/sites-enabled` directory by running the following command:

```bash
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
```

Alternatively, you can create a virtual host by creating a new configuration file in the `/etc/nginx/conf.d` directory. For example, you can create a file called `example.com.conf` by running the following command:

```bash
sudo nano /etc/nginx/conf.d/example.com.conf
```

Then you can add the following configuration to the file:

```nginx
server {
    listen 80;
    server_name example.com www.example.com;
    root /var/www/example.com;
    index index.html;
}
```


Then you can test the configuration by running the following command:

```bash
sudo nginx -t
```

If the configuration is correct, you can reload Nginx by running the following command:

```bash
sudo systemctl reload nginx
```

Finally, you need to create the root directory for the virtual host by running the following command:

```bash
sudo mkdir /var/www/example.com
sudo chown -R $USER:$USER /var/www/example.com
sudo chmod -R 755 /var/www/example.com
touch /var/www/example.com/index.html
echo "Hello, world!" > /var/www/example.com/index.html
```

Now you can open your web browser and go to `http://example.com` to see the virtual host in action.


