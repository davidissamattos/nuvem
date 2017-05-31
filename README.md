# nuvem
Raspberry Pi powered cloud (with lightning, thunder and rain)

## Configuration
### Basic packages
* `sudo apt-get update`
* `sudo apt-get install build-essential python-dev python-distlib python-setuptools python-pip python-wheel libzmq-dev libgdal-dev`

### Scientific packages
* `sudo apt-get install xsel xclip libxml2-dev libxslt-dev python-lxml python-h5py python-numexpr python-dateutil python-six python-tz python-bs4 python-html5lib python-openpyxl python-tables python-xlrd python-xlwt cython python-sqlalchemy python-xlsxwriter python-jinja2 python-boto python-gflags python-googleapi python-httplib2 python-zmq libspatialindex-dev`
* `sudo pip install bottleneck rtree`
* `sudo apt-get install python-numpy python-matplotlib python-mpltoolkits.basemap python-scipy python-sklearn python-statsmodels python-pandas`

### Install the files in requeriments.txt
* `pip install requirements.txt --user`

### Nginx
* Download nginx `sudo apt-get install nginx`
* Remove default site
    * `sudo rm /etc/nginx/sites-enabled/default`
* configure nginx as in http://www.onurguzel.com/how-to-run-flask-applications-with-nginx-using-gunicorn/

### Supervisor
* The file nuvem.conf should work if you download this git repo to your home directory
    * install supervisor `sudo apt-get install supervisor`
* configure supervisor
    * http://www.onurguzel.com/managing-gunicorn-processes-with-supervisor/
