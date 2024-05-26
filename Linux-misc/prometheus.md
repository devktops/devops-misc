Download the package 
```wget https://github.com/prometheus/prometheus/releases/download/v2.37.6/prometheus-2.37.6.linux-amd64.tar.gz```

Extract 
```tar xvfz prometheus-*.tar.gz```

Create two new directories for Prometheus to use. The /etc/prometheus directory stores the Prometheus configuration files. The /var/lib/prometheus directory holds application data.

```sudo mkdir /etc/prometheus /var/lib/prometheus```

Move into the main directory of the extracted prometheus folder. Substitute the name of the actual directory in place of prometheus-2.37.6.linux-amd64.

```cd prometheus-2.37.6.linux-amd64```

Move the prometheus and promtool directories to the /usr/local/bin/ directory. This makes Prometheus accessible to all users.

```sudo mv prometheus promtool /usr/local/bin/```

Move the prometheus.yml YAML configuration file to the /etc/prometheus directory.

```sudo mv prometheus.yml /etc/prometheus/prometheus.yml```

The consoles and console_libraries directories contain the resources necessary to create customized consoles. This feature is more advanced and is not covered in this guide. However, these files should also be moved to the etc/prometheus directory in case they are ever required.


```sudo mv consoles/ console_libraries/ /etc/prometheus/```

Verify that Prometheus is successfully installed using the below command:

```prometheus --version```

Create a prometheus user. The following command creates a system user.

sudo useradd -rs /bin/false prometheus

Assign ownership of the two directories created in the previous section to the new prometheus user.

sudo chown -R prometheus: /etc/prometheus /var/lib/prometheus

Run as a Service 

To allow Prometheus to run as a service, create a prometheus.service file using the following command:

```sudo vi /etc/systemd/system/prometheus.service```

Enter the following content into the file:

File: /etc/systemd/system/prometheus.service
```[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
Group=prometheus
Type=simple
Restart=on-failure
RestartSec=5s
ExecStart=/usr/local/bin/prometheus \
    --config.file /etc/prometheus/prometheus.yml \
    --storage.tsdb.path /var/lib/prometheus/ \
    --web.console.templates=/etc/prometheus/consoles \
    --web.console.libraries=/etc/prometheus/console_libraries \
    --web.listen-address=0.0.0.0:9090 \
    --web.enable-lifecycle \
    --log.level=info

[Install]
WantedBy=multi-user.target
```

Reload 
``` sudo systemctl daemon-reload ```

Enable - Start - Status 
``` 
sudo systemctl enable prometheus 
sudo systemctl start prometheus 
sudo systemctl status prometheus
```