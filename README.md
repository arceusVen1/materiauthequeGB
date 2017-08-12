# Mathériauthèque du Lycée Georges Brassens

----------

## Auteur:

```
jeremy.venin@telecom-sudparis.eu (arceusVen1)
gunjin.udval@telecom-sudparis.eu (gunjinudv)
```

Le but de ce projet est de permettre la création d'une matériauthèque modulaire et responsive 
permettant la gestion de différents matériaux et composites dans le cadre du lycée Georges Brassens.
 
 Le projet tourne sous Django-rest-framework et Python 3.6 au niveau du backend. Le frondend est géré par ReactJs avec Redux et Redux Saga.
 Son installation requiert donc au préalable la présence de Python 3.6 et éventuellement d'un 
 environnement virtuel sous cette version. 

 Afin d'éxécuter la version encore sous développement, il est également nécessaire de disposer
 de plusieurs packages python. Voici la suite de commande à éxécuter dans un environnement
 virtuel dans lequel se situe le projet afin de tester les fonctions pour l'instant implémentées.


 ```
 $ pip install -r requirements.txt
 $ python backend/manage.py migrate
 $ python backend/manage.py createsuperuser
 $ python backend/manage.py runserver
 ```

 Rendez vous maintenant sur ```http://localhost:8000/admin``` pour toute l'interface d'administration. L'API est elle disponible a ```http://localhost:8000/api/{materiaux, fournisseur, famille...}
 
### Bonnes Requêtes !
