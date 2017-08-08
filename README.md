By Price test
============

Requerimientos:
- python 3.6
- Nginx
- supervisor

## Contenido
- commons
- Instalando python
- Instalando y configurando Nginx
-  Instalando y configurando supervisor 

## commons
```sh
yum install openssl-libs
lsb_release -a
yum insall alternatives
yum install nginx
```

##instalando python

```sh
wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz
mv Python-3.6.1.tar.xz /usr/src/
tar -xf Python-3.6.1.tar.xz
cd Python-3.6.1
echo "\e[31mRead the fucking manual\e[0m" && less README.rst
./configure
make && make test && make install
python3.6 -V
```

### Creando un usuario y grupo de sustema.
En este caso usaremos la bandera `--system` tanto en useradd como en groupadd para poder decir que es de sistema y pueda acceder escalar en privilegios.
```
$ groupadd -r webapplication
$ useradd --system --gid webapplication -d /home/jenkins -s /bin/zsh jenkins

### Creando el directorio de trabajo para test
Una buena practica es hacer un directorio en el cual deba estar el proyecto/proceso y que este bajo el usuario y grupo de sistema creado. En este caso lo pondremos en `opt`, aunque bien podría esta en el home de jenkins o en `usr`. El lugar depende de cada uno y de que es lo que se deba poner. Si hablamos de crear un ejecutable, deberia estar en [/usr/sbin] si es de sistema, claro esta.
```

```
$ mkdir -p /opt/test/scrapapi_by_price
$ mkdir -p /opt/test/run/
$ mkdir -p /opt/test/envs/
$ mkdir -p /var/www/test/by_price/static
$ chown -R jenkins:webapplication /opt/test
$ chown -R www-data:webapplication /var/www/
$ chmod -R 771 /var/www/
```


## Configurando supervisor
```conf
[program:scrap]
autostart=true
autorestart=true
directory=/opt/test/scrapapi_by_price
command=/opt/test/scrapapi_by_price/start
user=jenkins
environment=
    DJANGO_SETTINGS_MODULE='tdev.settings.settings,
    URL_HOST='localhost',
    DB_NAME='products',
    DB_USER='by_price',
    DB_HOST='localhost',
    DB_PASSWD='jSKzh6&&*Sc^3yv!44MM*3BeSKZ95c',
    DEBUG='true',
    EMAIL_HOST_USER='',
    EMAIL_HOST_PASSWD='',
    STATIC_ROOT='/var/www/test/by_price',
autostart=true
autorestart=true
stdout_logfile=/var/log/jenkins.log
redirect_stderr=true
stopsignal=QUIT
```

```sh
#!/bin/bash
#set -x
NAME='scrap'
SOCKFILE=/opt/test/run/gunicorn.sock
USER=jenkins
GROUP=webapplication
NUM_WORKERS=4
DJANGO_WSGI_MODULE=testdev:wsgi

source venv/bin/active

cd /opt/test/scrapapi_by_price
gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user $USER --group=$GROUP \
    --bind unix:$SOCKFILE \
    --log-level info \
    --log-file /opt/test/logs/testdev.log
```

## Install and config nginx


```conf
mkdir -p /etc/nginx/sites-available
mkdir -p /etc/nginx/sites-enabled
```

Se debe abrir el archivo /etc/nginx/nginx.conf

```conf
include /etc/nginx/sites-enabled/*.conf;
server_names_hash_bucket_size 64;
```


```conf
upstream scrapapi {
    server unix:/opt/test/run/gunicorn.sock;
}
server{
listen 80;
listen [::]:80;

server_name servertest.com;
return 301 https://$host$request_uri;

location = /favicon.ico { access_log off; log_not_found off; }
location /static/ {
alias /var/www/test/by_price/static/;
}

location / {
include proxy_params;
proxy_pass http://scrapapi;
}

access_log /var/log/nginx/scrapapi/access.log;
error_log /var/log/nginx/scrapapi/error.log;
}

```

```sh
firewall-cmd --zone=public --permanent --add-service=http
firewall-cmd --reload
```

```sh
setsebool -P httpd_can_network_connect 1
```
## Creando el virtual enviroment

```
python3.6 -m venv /opt/test/envs/test
ln -s /opt/test/envs/test /opt/test/scrapapi_by_price/venv
```

```sh
#!/bin/zsh
set -x

echo -e "\e[1;32mActivando el enviroment  \e[0m"

source /path/to/new/virtual/environment/bin/activate

echo -e "\e[1;32mActivando las variables de entorno  \e[0m"

export URL_HOST=''
export DB_NAME=''
export DB_USER=''
export DB_HOST=''
export DB_PASSWD=''
export EMAIL_HOST_USER=''
export EMAIL_HOST_PASSWD=''
# write 'true' or 'false'
export DEBUG=''
export STATIC_ROOT=''
export REDIS_PREFIX=''
export REDIS_PASSWORD=''
export DJANGO_SETTINGS_MODULE=''
```
