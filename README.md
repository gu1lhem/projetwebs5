Ce qu'il reste à faire: 
- rendre les listes plus jolies, en affichant par exemple, plus de champs + widgets Date + centrage horizontal + page home
- intégrer csv 
- https://django-scheduler.readthedocs.io/en/latest/install.html
- créer les conditions: 
   - je ne peux pas mettre un étudiant de L2 dans un groupe de L3
   - je ne peux pas créer un cours si la salle/prof/groupe n'est pas
   dispo sur cette plage horaire



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
