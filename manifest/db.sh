#!/bin/bash

# Secure root account
sudo mysql -e "UPDATE mysql.user SET Password = PASSWORD('ondongoa') WHERE User = 'root'"
# Create database
sudo mysql -e "CREATE DATABASE IF NOT EXISTS identity"
# Create database
sudo mysql -e "CREATE DATABASE IF NOT EXISTS config_generator"
# Create application account
sudo mysql -e "GRANT ALL ON *.* TO 'identity'@'localhost' IDENTIFIED BY 'ondongoa' WITH GRANT OPTION;"
# Create application account
sudo mysql -e "GRANT ALL ON *.* TO 'config_generator'@'localhost' IDENTIFIED BY 'ondongoa' WITH GRANT OPTION;"
# Make our changes take effect
sudo mysql -e "FLUSH PRIVILEGES"