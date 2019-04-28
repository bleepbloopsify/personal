To configure the webserver

1. Use environment to specify which variables you'd like to exist locally. DO NOT EDIT .env file, that is for defaults only.



To deploy the fileserver

1. docker-compose up will bring up all services.

Certbot service should die on its own.

nginx will attach to port 80 and 443 and reverse proxy off of that.

To configure ssl run the certbot.sh script

Then set crontab to run renewcerts.sh over and over again.

Repos you want webhooks to manage will go into repos folder

Deploy keys go into keys folder

Fileserver data files go into data folder

Anything you want from the git repos should be hardlinked - not softlinked - into the data folder