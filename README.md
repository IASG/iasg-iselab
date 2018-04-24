# IASG ISELab
Shell and web applications to provision accounts and facilitate ISELab access.

## Installing
### Production
Configure any settings as needed in `iselab/settings_local.py`; see
`iselab/settings.py` for possible settings.

Add the following line to `/etc/sudoers` using `visudo`:
```
iasg    ALL=NOPASSWD: /usr/sbin/useradd, /usr/sbin/chpasswd
```
Run the following commands:
```
# useradd iasg
# groupadd iasg-users
# python3 -m pip install .
# cp scripts/nginx-vhost.conf /etc/nginx/{config-dir}/iselab.conf
# cat scripts/sshd_config >> /etc/ssh/sshd_config
# systemctl restart ssh
# systemctl start iselab.service
```

### Development
```
# Optionally create a virtual environment and source it
$ python3 -m venv env
$ source env/bin/activate
$ pip install -e .
$ ./iasg-web
$ ./iasg-login
```
Note that some components (e.g. adding users) will not work in development
without adding appropriate sudo rules.
