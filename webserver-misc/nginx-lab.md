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
sudo apt install nginx -y
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
    server_name 54.255.233.124 ec2-18-141-201-222.ap-southeast-1.compute.amazonaws.com;
    root /var/www/lab;
    index index.php index.html index.htm;
}
```

After creating the configuration file, you need to create a symbolic link to the `/etc/nginx/sites-enabled` directory by running the following command:

```bash
sudo ln -s /etc/nginx/sites-available/lab /etc/nginx/sites-enabled/
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

## Basic Authentication
You can add basic authentication to your virtual host's custom pages by creating a password file and adding the following configuration to the virtual host's configuration file:

```nginx
server {

    ## ....

    # Basic Authentication to admin directory
    location /admin {
        auth_basic "Restricted Area";
        auth_basic_user_file /etc/nginx/.htpasswd;
    }
}
```

You can create a password file by running the following command:

```bash
sudo apt install apache2-utils
sudo htpasswd -c /etc/nginx/.htpasswd username
```



## SSL Installation
You can install SSL by using certbot. You can install certbot by running the following commands:

```bash
sudo apt install certbot python3-certbot-nginx
```

Then you can obtain a certificate by running the following command:

```bash
sudo certbot --nginx
```

You will be prompted to enter your email address and agree to the terms of service. After that, certbot will automatically obtain and install a certificate for your domain.

## SSL Auto-Renewal
You can set up auto-renewal for your SSL certificate by creating a cron job. You can do this by running the following command:

```bash
sudo crontab -e
```

Then you can add the following line to the crontab file: to renew the certificate every month

```bash
0 0 1 * * certbot renew --quiet --force-renewal --nginx > /var/log/letsencrypt-renew.log 2>&1
```

Finally, you can save the file and exit the editor. Now your SSL certificate will be automatically renewed every month.
```

