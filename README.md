
# Installation :


```bash
git clone git@github.com:f14ke/projetwebs5.git
cd projetwebs5
python -m venv env
. env/bin/activate
pip install -m wheel
pip install -r requirements.txt
pip install git+https://github.com/f14ke/django-scheduler.git
sudo apt install npm
sudo npm install -g bower
export DJANGO_SETTINGS_MODULE=Projetweb.settings
python manage.py bower install
python manage.py migrate
python manage.py collectstatic
```

# Informations :

Attention : nous utilisons un fork non publié de *django-scheduler*. Le terme " django-scheduler " **ne doit pas** se retrouver dans *requirements.txt*. Pour mettre à jour ce librairie :
pip install --upgrade git+https://github.com/f14ke/django-scheduler.git
