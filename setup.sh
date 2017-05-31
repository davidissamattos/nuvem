#!/usr/bin/env bash
sudo cp /home/pi/nuvem/nuvem.conf /etc/nginx/sites-available/nuvem.conf
sudo ln -s /etc/nginx/sites-available/nuvem.conf /etc/nginx/sites-enabled/
nginx -t
sudo service nginx reload

sudo cp /home/pi/nuvem/supervisor_nuvem.conf /etc/supervisor/conf.d//supervisor_nuvem.conf
supervisorctl reread
supervisorctl update
supervisorctl start nuvem


