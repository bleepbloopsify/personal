#!/bin/bash

cd /home/pa_ssion/github/personal/resourceserver/

docker-compose run certbot certbot certonly\
  --agree-tos \
  --webroot -w /var/www \
  -d fileserver.bleepbloopsify.io \
  -d webhooks.fileserver.bleepbloopsify.io