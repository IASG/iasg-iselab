# IASG ISELab
Shell and web applications to provision accounts and facilitate ISELab access.

## Installing
### Production
Add the following line to `/etc/sudoers` using `visudo`:
```
iasg    ALL=NOPASSWD: /usr/sbin/useradd, /usr/sbin/chpasswd
```
Run the following commands:
```
$ sudo useradd iasg
$ sudo groupadd iasg-users
$ sudo python3 setup.py install
$ sudo cp scripts/nginx-vhost.conf /etc/nginx/{config-dir}/iselab.conf
$ cat scripts/sshd_config | sudo tee -a /etc/ssh/sshd_config
$ sudo systemctl restart ssh
$ sudo systemctl start iselab.service
```

### Development
```
$ python3 setup.py develop
./iasg-web
./iasg-login
```
