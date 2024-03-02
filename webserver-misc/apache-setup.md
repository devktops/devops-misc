Here is a step-by-step guide to setting up a basic Apache virtual host configuration.
1. **Install Apache**  
Ensure that Apache is installed on your server. On Ubuntu, you can install it using:
```cmd
sudo apt update
sudo apt install apache2
```

2. **Create the Document Root**  
Create a directory for your domain where the website files will live:
       
```cmd
sudo mkdir -p /var/www/domain.com/public_html
```

3. **Set Permissions**  
Adjust the permissions to ensure that the web content can be accessed:
```cmd
sudo chown -R $USER:$USER /var/www/domain.com/public_html
sudo chmod -R 755 /var/www
```

4. **Create a Sample Page (Optional)**  
Create a sample `index.html` file in your document root to test the setup:
```html
<html>
    <head>
        <title>Welcome to Your_domain!</title>
    </head>
    <body>
        <h1>Success!  The your_domain virtual host is working!</h1>
    </body>
</html>
```

5. **Create Apache Virtual Host File**  
Copy the default configuration file to create a new virtual host file:
```cmd
sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/domain.com.conf
```

6. **Edit the Virtual Host File**  
Open the newly created configuration file in a text editor:
```cmd
sudo nano /etc/apache2/sites-available/domain.com.conf
```
Then, modify it to match the following setup, adjusting ServerAdmin, ServerName, ServerAlias, and DocumentRoot as needed:
```apache
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    ServerName domain.com
    ServerAlias www.domain.com
    DocumentRoot /var/www/domain.com/public_html
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

7. **Enable the Virtual Host**  
Enable the new site configuration using `a2ensite`:
```
sudo a2ensite domain.com.conf
```

8. **Disable the Default Site (Optional)**  
If you wish, disable the default site to prevent it from interfering:
```
sudo a2dissite 000-default.conf
```

9. **Reload Apache**  
Reload Apache to apply the changes:
```
sudo systemctl reload apache2
```

10. **Test Your Setup**  
Open your web browser and go to `http://domain.com`. You should see your "Hello, World!" page or the content you've placed in the document root.

    
