#!/usr/bin/env bash
#configuration of nginx
sudo cp /home/pi/nuvem/conf/nginx_nuvem.conf /etc/nginx/sites-available/nuvem.conf
sudo ln -s /etc/nginx/sites-available/nuvem.conf /etc/nginx/sites-enabled/
sudo nginx -t
sudo service nginx reload

#configuration of the supervisor
sudo cp /home/pi/nuvem/conf/supervisor_nuvem.conf /etc/supervisor/conf.d/supervisor_nuvem.conf
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start nuvem


