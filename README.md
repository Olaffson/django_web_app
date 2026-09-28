# django_web_app

Application Django d'apprentissage (projet `merchex`, application `listings`).

## Pages

| URL           | Description                      |
|---------------|----------------------------------|
| `/hello/`     | Liste des groupes (`Band`)       |
| `/listings/`  | Liste des annonces (`Listing`)   |
| `/about-us/`  | Page « À propos »                |
| `/admin/`     | Interface d'administration       |

## Lancer en local

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
cd merchex
python manage.py migrate
DJANGO_DEBUG=True python manage.py runserver
```

Créer un compte administrateur : `python manage.py createsuperuser`.

Lancer les tests : `python manage.py test` (depuis le dossier `merchex`).

## Lancer avec Docker

```bash
docker compose up -d --build
docker compose down
```

L'application est disponible sur http://localhost:8000/hello/.

## Variables d'environnement

| Variable               | Défaut                   | Rôle                                      |
|------------------------|--------------------------|-------------------------------------------|
| `DJANGO_SECRET_KEY`    | clé de développement     | À définir obligatoirement en production   |
| `DJANGO_DEBUG`         | `False`                  | `True` pour le développement              |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1`    | Hôtes autorisés, séparés par des virgules |
