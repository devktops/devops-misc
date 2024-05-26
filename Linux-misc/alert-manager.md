### Install Alert Manager 

Download 
```
wget https://github.com/prometheus/alertmanager/releases/download/v0.26.0/alertmanager-0.26.0.linux-amd64.tar.gz
```
Unzip file 
```
tar -xvf alertmanager-0.26.0.linux-amd64.tar.gz
cd alertmanager-0.26.0.linux-amd64
```

Create User and Group fro Alert Manager
```
sudo groupadd -f alertmanager
sudo useradd -g alertmanager --no-create-home --shell /bin/false alertmanager
```
Make Directories and give permission 

```
sudo mkdir -p /etc/alertmanager/templates
sudo mkdir /var/lib/alertmanager
udo chown alertmanager:alertmanager /etc/alertmanager
sudo chown alertmanager:alertmanager /var/lib/alertmanager
```
Copy to executable file 
```
sudo cp alertmanager /usr/bin/
sudo cp amtool /usr/bin/
sudo chown alertmanager:alertmanager /usr/bin/alertmanager
sudo chown alertmanager:alertmanager /usr/bin/amtool
sudo cp alertmanager.yml /etc/alertmanager/alertmanager.yml
sudo chown alertmanager:alertmanager /etc/alertmanager/alertmanager.yml
```

Run as a Service 

```
sudo vi /etc/systemd/system/alertmanager.service
```

Copy and past the following content 
```
[Unit]
Description=AlertManager
Wants=network-online.target
After=network-online.target

[Service]
User=alertmanager
Group=alertmanager
Type=simple
ExecStart=/usr/bin/alertmanager \
    --config.file /etc/alertmanager/alertmanager.yml \
    --storage.path /var/lib/alertmanager/

[Install]
WantedBy=multi-user.target
```
Reload 
``` 
sudo systemctl daemon-reload
 ```

Enable - Start - Status 
``` 
sudo systemctl enable alertmanager 
sudo systemctl start alertmanager
sudo systemctl status alertmanager
```

Default port : 9093

