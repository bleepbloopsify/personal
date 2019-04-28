#!/bin/bash

# This file is only for certifying specific uris.

docker-compose run certbot certbot certonly \
  --agree-tos \
  --webroot -w /var/www \
  -d fileserver.bleepbloopsify.io \
  -d webhooks.fileserver.bleepbloopsify.io