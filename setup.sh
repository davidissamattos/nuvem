#!/usr/bin/env bash
#configuration of nginx
sudo cp /home/pi/nuvem/nuvem.conf /etc/nginx/sites-available/nuvem.conf
sudo ln -s /etc/nginx/sites-available/nuvem.conf /etc/nginx/sites-enabled/
nginx -t
sudo service nginx reload

#configuration of the supervisor
sudo cp /home/pi/nuvem/supervisor_nuvem.conf /etc/supervisor/conf.d//supervisor_nuvem.conf
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start nuvem


