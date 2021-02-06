
# Installation :


```bash
git clone git@github.com:f14ke/projetwebs5.git
cd projetwebs5
python -m venv env
. env/bin/activate
pip install -m wheel
pip install -r requirements.txt
sudo apt install npm
sudo npm install -g bower
export DJANGO_SETTINGS_MODULE=Projetweb.settings
python manage.py bower install
python manage.py migrate
```
