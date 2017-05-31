#!/bin/env bash
cp /home/pi/nuvem.conf /etc/nginx/sites-available/nuvem.conf
sudo ln -s /etc/nginx/sites-available/nuvem.conf /etc/nginx/sites-enabled/
nginx -t
sudo service nginx reload


