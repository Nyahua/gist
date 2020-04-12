# [How To Serve Flask Applications with Gunicorn and Nginx on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04)

## Install Nginx
```bash
sudo apt update
sudo apt install nginx

sudo ufw allow 'Nginx HTTP'
sudo ufw status

systemctl status nginx

# get my IP address
ip addr show eth0 | grep inet | awk '{ print $2; }' | sed 's/\/.*$//'
# or
curl -4 icanhazip.com

# Managing the Nginx Process
sudo systemctl stop nginx
sudo systemctl start nginx
sudo systemctl restart nginx
# reload without dropping connections
sudo systemctl reload nginx

sudo systemctl disable nginx
sudo systemctl enable nginx
sudo systemctl status nginx

# force remove
sudo apt-get purge nginx nginx-common nginx-full
sudo apt-get install nginx
```

## Step 1 — Installing the Components from the Ubuntu Repositories
```bash
sudo apt update
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
```
## Step 2 — Creating a Python Virtual Environment
```bash
sudo apt install python3.8
sudo apt install python3.8-venv
mkdir wsgiportal
cd wsgiportal
python3.8 -m venv portalenv
source portalenv/bin/activate
pip install wheel
pip install gunicorn flask
```
### Creating a Sample App
```bash
nano portal.py
```
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
```
```bash
sudo ufw allow 5000
python portal.py
```
### Creating the WSGI Entry Point
```bash
nano wsgi.py
```
```python
from portal import app

if __name__ == "__main__":
    app.run()
```
We can do this by simply passing it the name of our entry point. This is constructed as the name of the module (minus the `.py` extension), plus the name of the callable within the application. In our case, this is `wsgi:app`.
```bash
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

We’re now done with our virtual environment, so we can deactivate it:

```bash
deactivate
```

# Creating a WSGI Configuration File
```bash
mkdir config
nano config/portal.service
```
```json
[Unit]
Description=Gunicorn instance to serve portal
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/wsgiportal
Environment="PATH=/home/ubuntu/wsgiportal/portalenv/bin"
ExecStart=/home/ubuntu/wsgiportal/portalenv/bin/gunicorn --workers 3 --bind unix:portal.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```
[Typically in ubuntu, nginx runs as www-data. If defined www-data as the group for gunicorn, you can solve this problem by:]
(https://stackoverflow.com/questions/41951792/gunicorn-and-django-error-permission-denied-for-sock)
```bash
chmod g+x /home/ubuntu/
chmod g+r /home/ubuntu/
sudo chgrp www-data /home/ubuntu/
```
```bash
sudo cp config/portal.service /etc/systemd/system/
sudo systemctl start portal
sudo systemctl enable portal
sudo systemctl status portal
```

### Step 5 — Configuring Nginx to Proxy Requests
```bash
nano config/portal
```
```json
server {
    listen 80;
    server_name 111.229.0.74;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/wsgiportal/portal.sock;
    }
}
```
```bash
sudo cp config/portal /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/portal /etc/nginx/sites-enabled

sudo nginx -t
sudo ufw allow 'Nginx Full'
sudo systemctl restart nginx
```
> If you encounter any errors, trying checking the following: 
```bash
sudo less /var/log/nginx/error.log # checks the Nginx error logs. 
sudo less /var/log/nginx/access.log # checks the Nginx access logs.
sudo journalctl -u nginx # checks the Nginx process logs.
sudo journalctl -u portal  # checks your Flask app’s Gunicorn logs.
```
