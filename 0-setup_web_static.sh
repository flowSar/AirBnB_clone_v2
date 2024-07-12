#!/usr/bin/env bash
# doesn some I'm tired from it
sudo apt update
NGINX_INSTALLED=$(nginx -v 2>&1)
if ! echo "$NGINX_INSTALLED" | grep -q "nginx"; then
    sudo apt -y install nginx
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
uri="$uri"
sudo cp $CONFIG_FILE ${CONFIG_FILE}.bak
# Add the location block to the Nginx configuration file if it does not exist
if ! grep -q "location /hbnb_static" $CONFIG_FILE; then
    sudo sed -i "56i \\\tlocation /hbnb_static {\n \\t \\talias /data/web_static/current/;\n \\t \\ttry_files ${uri} /index.html =404; \n\\t}" $CONFIG_FILE

fi

sudo systemctl restart nginx
