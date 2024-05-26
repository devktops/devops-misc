### Config Node Exporter on Client 
Ref : https://prometheus.io/download/#node_exporter 

Download 
```
wget https://github.com/prometheus/node_exporter/releases/download/v1.5.0/node_exporter-1.5.0.linux-amd64.tar.gz
```

Extract the app 

```
tar xvfz node_exporter-*.tar.gz
```

Move to executable 

``` 
sudo mv node_exporter-1.5.0.linux-amd64/node_exporter /usr/local/bin 
```

Run as a service 
```
sudo useradd -rs /bin/false node_exporter
```
Create a service file for systemctl to use. The file must be named node_exporter.service

```
sudo vi /etc/systemd/system/node_exporter.service
```

File: /etc/systemd/system/node_exporter.service
```
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
Restart=on-failure
RestartSec=5s
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=multi-user.target
```
Reload 
``` 
sudo systemctl daemon-reload
 ```

Enable - Start - Status 
``` 
sudo systemctl enable node_exporter
sudo systemctl start node_exporter
sudo systemctl status node_exporter
```