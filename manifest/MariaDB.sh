#!/bin/bash

# Installation des dépendances
pip install --upgrade pip &&
sudo apt-get update && 
sudo apt-get install mariadb-server -y && 
sudo /etc/init.d/mysql start &&
pip install mysql-connector-python

# Configuration de la base de données
mysql -u root -pondongoa -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY 'ondongoa' WITH GRANT OPTION; FLUSH PRIVILEGES;"
mysql -u root -pondongoa -e "create database identity; create database config_generator;"
mysql -u root -pondongoa -e "use identity; create table users(user_id INTEGER auto_increment PRIMARY KEY, user_nom VARCHAR(255) not null, user_prenom VARCHAR(255) not null, user_date DATE not null)ENGINE=InnoDB; create table usernames(user_id INTEGER auto_increment PRIMARY KEY, username VARCHAR(255) not null, password VARCHAR(255) not null)ENGINE=InnoDB;"
mysql -u root -pondongoa -e "use config_generator; CREATE TABLE webserver (id INT(11) NOT NULL AUTO_INCREMENT, root_path VARCHAR(255) NOT NULL, index_files VARCHAR(255) NOT NULL, error_page VARCHAR(255) NOT NULL, error_page_path VARCHAR(255) NOT NULL, PRIMARY KEY (id)) ENGINE=InnoDB; CREATE TABLE reverse_proxy (id INT(11) NOT NULL AUTO_INCREMENT, strategy_method VARCHAR(255) NOT NULL, server1_domain VARCHAR(255) NOT NULL, server2_domain VARCHAR(255) NOT NULL, PRIMARY KEY (id)) ENGINE=InnoDB; CREATE TABLE load_balancer (id INT(11) NOT NULL AUTO_INCREMENT, app_path VARCHAR(255) NOT NULL, proxy_bind VARCHAR(255) NOT NULL, proxy_pass VARCHAR(255) NOT NULL, webserver_id INT(11) NOT NULL, PRIMARY KEY (id), CONSTRAINT fk_load_balancer_webserver FOREIGN KEY (webserver_id) REFERENCES webserver(id)) ENGINE=InnoDB;"
mysql -u root -pondongoa -e "use identity; INSERT INTO users (user_nom, user_prenom, user_date) VALUES ('alex', 'ondongo', '2000-01-01'), ('daryl', 'ondongo', '1998-05-15'), ('boss', 'trap', '1995-11-30'); INSERT INTO usernames (username, password) VALUES ('alex', 'ondongoa'), ('daryl', 'password'), ('boss', 'pass123');"
mysql -u root -pondongoa -e "use config_generator; INSERT INTO webserver (root_path, index_files, error_page, error_page_path) VALUES ('/var/www/html', 'index.html index.htm', '404 Not Found', '/var/www/html/error.html'); INSERT INTO reverse_proxy (strategy_method, server1_domain, server2_domain) VALUES ('round-robin', 'server1.example.com', 'server2.example.com'); INSERT INTO load_balancer (app_path, proxy_bind, proxy_pass, webserver_id) VALUES ('/app', '127.0.0.1:8080', 'http://server1.example.com', 1);"