# IASG ISELab
Shell and web applications to provision accounts and facilitate ISELab access.

## Installing
### Production
```
$ sudo python3 setup.py install
$ sudo cp nginx-vhost.conf /etc/nginx/{config-dir}/iselab.conf
$ iasg-web
```

### Development
```
$ python3 setup.py develop
./iasg-web
./iasg-login

```