# Spotify Analytics Backend

Ce projet constitue le backend de l'application Spotify Analytics, développé avec Django et Django REST framework. Il permet de récupérer, stocker et analyser les données d'écoute des utilisateurs depuis l'API Spotify.

## Prérequis

- Python 3.x
- Django
- Django REST framework
- Celery
- Redis
- Spotipy

## Installation

### Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/spotify-analytics-backend.git
cd spotify-analytics-backend
```

### Créer un environnement virtuel

```bash
python -m venv env
source env/bin/activate  # Sur Windows : env\Scripts\activate
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

### Configurer les variables d'environnement

Créez un fichier `.env` dans le répertoire principal et ajoutez vos configurations :

```env
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
```

### Appliquer les migrations

```bash
python manage.py migrate
```

### Créer un superutilisateur

```bash
python manage.py createsuperuser
```

### Démarrer le serveur de développement

```bash
python manage.py runserver
```

### Configurer Celery et Redis

Assurez-vous que Redis est installé et en cours d'exécution. Démarrez Celery avec les commandes suivantes :

```bash
celery -A myspotifyapp worker --loglevel=info
celery -A myspotifyapp beat --loglevel=info
```

### Endpoints de l'API

| Endpoint	              | Description                             |
| :-----------------------| :-------------------------------------: |
| /api/recent-tracks/	    | Récupère les morceaux récemment écoutés |
| /api/top-artists/	      | Récupère les artistes les plus écoutés  |
| /api/top-tracks/        |	Récupère les morceaux les plus écoutés  |
| /api/listening-history/ |	Récupère l'historique d'écoute          |
| /api/top-genres/	      | Récupère les genres les plus écoutés    |

### Documentation
- [Django](https://docs.djangoproject.com/en/5.0/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)
- [Redis](https://redis.io/)
- [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/)


### Contribuer

Les contributions sont les bienvenues ! Veuillez ouvrir une issue ou soumettre une pull request.

### Licence

Ce projet est sous licence MIT.