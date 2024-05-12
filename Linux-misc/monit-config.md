For Monit Dashboard 

```
set httpd port 2812 and     
    use address 0.0.0.0    
    allow 0.0.0.0/0    
    allow admin:monit
```
For Gmail SMTP setup 

```
set mailserver smtp.gmail.com port 587
    username "youremail@gmail.com" password "your App password" 
    using tls
```

For Email Template Format 
```
set mail-format {
   from:    Monit <monit@$HOST>
   subject: monit alert --  $EVENT $SERVICE
   message: $EVENT Service $SERVICE
                 Date:        $DATE
                 Action:      $ACTION
                 Host:        $HOST
                 Description: $DESCRIPTION

            Your DevOps Blah...
            Monit
 }
 ```

 Email Address to send alert 
 ```
 set alert yourreceivingemail@gmail.com
 ```