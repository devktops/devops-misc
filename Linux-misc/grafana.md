

Install some required utilities using apt.

``` 
sudo apt-get install -y apt-transport-https software-properties-common 
```

Import the Grafana GPG key.

```
sudo wget -q -O /usr/share/keyrings/grafana.key https://apt.grafana.com/gpg.key
```

Add the Grafana “stable releases” repository.

```
echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```

Update the packages in the repository, including the new Grafana package.

```
sudo apt-get update
```

Install the open-source version of Grafana.


```
sudo apt-get install grafana
```

Reload the systemctl daemon.

```
sudo systemctl daemon-reload
```

Enable and start the Grafana server. Using systemctl enable configures the server to launch Grafana when the system boots.

```
sudo systemctl enable grafana-server.service

sudo systemctl start grafana-server
```

Verify the status of the Grafana server and ensure it is in the active state.

```
sudo systemctl status grafana-server
```

