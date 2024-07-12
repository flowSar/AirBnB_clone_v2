#!/usr/bin/env bash
# doesn some I'm tired from it
HOSTNAME=$(hostname)

NGINX_INSTALLED=$(nginx -v 2>&1)
if ! echo "$NGINX_INSTALLED" | grep -q "nginx"; then
    sudo apt-get update > /dev/null
    sudo apt-get -y install nginx > /dev/null
fi
# create folder and index.html
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html

# inject simple html content in index.html
sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# check if symbol exsite and delete it 
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
# creat symbolic link
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group and everything inside
sudo chown -R ubuntu:ubuntu /data/

CONFIG_FILE="/etc/nginx/sites-available/default"
sudo cp $CONFIG_FILE ${CONFIG_FILE}.bak
# Add the location block to the Nginx configuration file if it does not exist

if ! grep -q "^ *location /hbnb_static {" /etc/nginx/sites-available/default; then
	sed -i '/server_name _;/a\
\
	location /hbnb_static {\
		alias /data/web_static/current/;\
		autoindex off;\
	}' /etc/nginx/sites-available/default
fi

sudo service nginx restart
