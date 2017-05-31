# nuvem
Raspberry Pi powered cloud (with lightning, thunder and rain)

## Configuration
* Install python-dev `sudo apt-get install python-dev`
* Download nginx `sudo apt-get install nginx`
### Install the files in requeriments.txt
* `pip install requirements.txt --user`

* configure nginx as in http://www.onurguzel.com/how-to-run-flask-applications-with-nginx-using-gunicorn/
* The file nuvem.conf should work if you download this git repo to your home directory
    * install supervisor `sudo apt-get install supervisor`
* configure supervisor
    * http://www.onurguzel.com/managing-gunicorn-processes-with-supervisor/
