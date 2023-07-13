# Utilisez une image de base appropriée qui prend en charge SQLite
FROM python:3

# Copiez le fichier de base de données dans le conteneur
COPY merchex/db.sqlite3 /app/db.sqlite3
COPY requirements.txt /app/requirements.txt

# Définir le répertoire de travail
WORKDIR /app

RUN apt-get update

# Installez les dépendances si nécessaire
RUN pip install -r requirements.txt

# Exécutez les commandes nécessaires pour initialiser votre base de données, si nécessaire
# RUN python manage.py migrate

# Commande par défaut pour exécuter le conteneur
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]