
Ceci est l'interface utilisateur de notre logiciel de traitement d'image.

Pour l'utiliser, lancer le fichier python main.py dans un environnement contenant tous les modules nécessaires.
Choisir quelle image source et target que l'on désire, puis la fonctionnalité erase ou insert, puis lancer le bouton Run.

Dans la première fenêtre qui s'affiche, choisir l'élément à envoyer sur l'image target avec deux clics de manière à former un rectangle.
Dans la deuxième, choisir ou coller l'image source.

Ceci est une version alpha de l'interface utilisateur. On pourra théoriquement choisir n'importe quelle image. Par ailleurs, l'implementation erase est mal implantée car necessiterait d'inverser source et target.
En effet, afin d'erase, il faut choisir une aone "vide" (comme de l'eau) dans la source, puis choisir l'élément à supprimer dans la target.

