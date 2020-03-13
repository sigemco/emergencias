sudo apt install redis python-virtualenv
virtualenv -p python3 entornovirtual
source entornovirtual/bin/activate
pip install -r requerimientos.txt
cd  proyecto
python manage.py migrate
python manage.py createsuperuser
