## your vps infomation here:

## useful links:

- https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04
- https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-18-04
- https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-18-04
- https://www.digitalocean.com/community/tutorials/how-to-install-run-connect-to-jupyter-notebook-on-remote-server
- https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
- https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04
- https://www.linuxbabe.com/linux-server/setup-your-own-shadowsocks-server-on-debian-ubuntu-centos
- https://github.com/233boy/v2ray


## vps@vultr
- https://my.vultr.com/  login: 140deport@outlook pw:FirstCar
- ssh ip: `198.13.32.35` karibu@henglong@vultr
- ```c
ssh karibu@198.13.32.35 -o "ServerAliveInterval 60" -o "ServerAliveCountMax 120"
```

- diable timeout: add following line by `sudo nano /etc/ssh/ssh_config`
```bash
ServerAliveInterval 60
ServerAliveCountMax 120
```

### Generate a new ED25519 SSH key pair:
```bash
ssh-keygen -t ed25519 -C "email@example.com"
# Or, if you want to use RSA:
ssh-keygen -t rsa -b 4096 -C "email@example.com"
```
The -C flag adds a comment in the key in case you have multiple of them and want to tell which is which. It is optional.

copy the key, under WSL / GNU/Linux (requires the xclip package):
```bash
xclip -sel clip < ~/.ssh/id_ed25519.pub
# Git Bash on Windows:
cat ~/.ssh/id_ed25519.pub | clip
```
