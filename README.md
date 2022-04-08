# Webinaire HOWL Django: Django, HTMX et Alpine.js. Un mariage parfait ?

L'objectif de ce webinaire et d'introduire l'auditeur à mes réflexion et aux tendances qu'on
observe aujourd'hui dans le développment Django. Nous allons parler de la HOWL (HTML over
whatever backend language you want) et voir htmx et alpine.js peuvent être utilisés pour fluidifier
et, dans une certaine meure simplifier le développement django.

## Installation du projet

Une fois cloné sur votre ordinateur, les dépendances de ce projet peut être facilement installé à l'aide de pipenv, conformément aux recommandations de la [documentation officielle](https://packaging.python.org/en/latest/tutorials/managing-dependencies/). Si pipenv n'est pas encore installé sur votre ordinateur, vous trouverez des instuctions d'installation détaillées [sur cette page](docs/pipenv/installation-fr.md).

Voici donc les instructions pour installer le projet jusqu'à l'exécution du serveur de développement:

1. Cloner ce dépôt de code à l'aide de la commande `$ git clone https://github.com/placepython/webinaire-htmx-avril-2022.git webinaire-html`.
2. Rendez-vous depuis un terminal à la racine du répertoire webinaire-htmx avec la commande `$ cd webinaire-html`
3. Installez les dépendances du projet à l'aide de la commande `pipenv install` (pipenv doit [au préalable avoir été installé](docs/pipenv/installation-fr.md))
4. Créer et alimenter la base de données à l'aide de la commande `pipenv run python manage.py create_db`
5. Démarrer le serveur avec `pipenv run python manage.py runserver`

Le serveur de développement peut être stoppé à l'aide de CTRL-C lorsqu'il est lancé.

