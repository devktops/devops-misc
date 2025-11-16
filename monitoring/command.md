
### Create a Docker Network 
`docker network create lab-network`

### Build Applicatin Container 
`docker build -t lab-app .` 

### Run Docker Container 
`docker run --network lab-network -p 8000:8000 -d lab-app`

### Setup Prometheus Script 
```global:
scrape_interval: 5s  # Set the interval to scrape targets

scrape_configs:
  - job_name: 'python_app'
    static_configs:
      - targets: ['container_name:8000']  # Adjust to match the Python app’s metrics endpoint
```

### Run Prometheus Container 
`docker run -d --name prometheus --network lab-network -p 9090:9090 -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus`

### Run the grafana Container 
`docker run -d --name=grafana -p 3000:3000 grafana/grafana`

###  Setup Node Exporter 
`docker run -d --name=node-exporter --net="host" prom/node-exporter` 

### To Reload Prometheus Container 
``` Stop the current prometheus container and rm 
docker stop container_name or id 
docker rm container_name or id 
Update the prometheus.yml file and run the prometheus 
```