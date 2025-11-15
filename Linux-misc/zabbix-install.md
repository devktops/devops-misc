# Zabbix  Server Installation

- Install Zabbix on Ubuntu 22.04

```bash
sudo apt update 
wget https://repo.zabbix.com/zabbix/6.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.0-4+ubuntu22.04_all.deb  
sudo dpkg -i zabbix-release_6.0-4+ubuntu22.04_all.deb 
sudo apt update 
```

- Config Zabbix Server

```bash
sudo apt install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent
```

- Install Mariadb and setup Zabbix Database

```bash
sudo apt install mariadb-server 
mysql -u root -p -> enter 
mysql> create database zabbix character set utf8mb4 collate utf8mb4_bin;
mysql> create user zabbix@localhost identified by 'password';
mysql> grant all privileges on zabbix.* to zabbix@localhost;
mysql> set global log_bin_trust_function_creators = 1;
mysql> quit;
```

- Import Zabbix initial schema

```bash
zcat /usr/share/zabbix-sql-scripts/mysql/server.sql.gz | mysql --default-character-set=utf8mb4 -uzabbix -p zabbix
```

- Configure the database for Zabbix

```bash
sudo vim /etc/zabbix/zabbix_server.conf
```

- Uncomment DBPassword and add password for the Zabbix
- Start and enable Zabbix server and agent

```bash
sudo systemctl restart zabbix-server zabbix-agent apache2
sudo systemctl enable zabbix-server zabbix-agent apache2
```

- Browse to the Zabbix Dashboard and setup the dashboard

```bash
http://your_ip/zabbix 
Login with default password "Admin:zabbix" 
```

Ref : https://www.zabbix.com/download?zabbix=6.4&os_distribution=ubuntu&os_version=24.04&components=server_frontend_agent&db=mysql&ws=apache

## Zabbix Agent Installation 
- Login to the agent server

```bash
sudo apt update
wget https://repo.zabbix.com/zabbix/6.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.0-4+ubuntu22.04_all.deb  
sudo dpkg -i zabbix-release_6.0-4+ubuntu22.04_all.deb 
sudo apt update 
sudo apt install zabbix-agent
```

- Config zabbix agent

```bash
sudo vim /etc/zabbix/zabbix_agentd.conf
```

- Fine the following lines and replace

```bash
Server=<YourZabbix_Server_IP>
```

- Start and enable Zabbix agent service

```bash
sudo systemctl start zabbix-agent
sudo systemctl enable zabbix-agent 
sudo systemctl status zabbix-agent 
```
After this, add the host in Zabbix dashboard. 