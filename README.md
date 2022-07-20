# Edition d'images de Poisson
### Sébastien Boisgérault, MINES ParisTech


*La photo ci-dessous a subi une retouche significative. Mais laquelle ? (Réponse dans la suite)* 

![](figs/objects-final.jpeg)

Contexte
--------------------------------------------------------------------------------

Restaurer des portions d'images inconnues ou endommagées de façon crédible 
est un problème important en édition d'images. Avec ce type de fonctionnalité 
de base disponible, d'autres en découlent ; ainsi
pour dissimuler un bouton disgracieux dans un portrait,
il suffit de désigner volontairement cette petite zone comme endommagée puis 
de laisser l'algorithme "réparer"[^0] la région en utilisant le reste de
l'image. 

[^0]: Dans le programme d'édition d'image GIMP, la fonctionnalité s'appelle
le *correcteur* dans le documentation française. Il est désigné par un sparadrap et sous le
nom *heal tool* dans la version anglaise.

La solution dite "de Poisson" à ce problème consiste au final[^1] à attribuer 
à chaque pixel dont la couleur est inconnue une couleur qui soit la 
moyenne des couleurs de ses voisins immédiats. 
Comme ces couleurs peuvent également être inconnues, 
la résolution du problème passe par l'inversion d'un (potentiellement gros) système d'équations 
linéaires.

[^1]: La présentation théorique de la technique décrit le plus souvent les
images comme des fonctions $u$ de variables continues $x, y \in \mathbb{R}$.
On cherche alors à résoudre l'équation de Poisson $\Delta u(x, y) = 0$ avec des
conditions au bord de type Dirichlet, un problème bien connu des physiciens.

--------------------------------------------------------------------------------

*L'image originale (ci-dessous) comportait un objet supplémentaire : une montre.
Elle a été recouverte dans l'image retouchée par des greffons prélevés dans une zone sans objet, 
de même texture que le reste de l'arrière plan. La technique de Poisson
utilisée ne laisse aucune trace de "couture" sur les bords de la greffe, 
ce qui rend la retouche assez crédible. 
([Photographie originale par Vadim Sherbakov](https://unsplash.com/photos/tCICLJ5ktBE), 
[licence Unsplash Creative Commons Zero](https://unsplash.com/license))*

![](figs/objects.jpeg)



Objectifs
--------------------------------------------------------------------------------

Ce projet implémentera la méthode dite "de Poisson" pour l'édition
d'image.  

Le projet se prête à un développement très progressif. 
La réalisation d'un prototype qui interprête 
dans une image tous les points (purement) rouge comme des zones abimées 
et les remplace par la solution de l'équation de Poisson associée est 
relativement simple.
Mais il existe ensuite de très nombreuses façons potentielles d'améliorer 
cette version initiale et de relever le niveau de difficulté de l'exercice ; 
notamment (indicatif):

  - En rajoutant des fonctionnalités. Par exemple en supportant l'utilisation
    de greffons spécifiques pour la réparation des zones endommagées plutôt
    qu'en utilisant uniquement les valeurs de l'image en bord de cette zone 
    (support de l'interpolation guidée ; cf exemple d'usage dans les
    fig. 1 et 2). 

  - En améliorant la performance de l'application. Le prototype initial sera 
    vraisemblablement (très) lent, 
    et ce d'autant plus que les zones endommagées seront grandes. Ce problème
    peut être attaqué de deux façons complémentaires : d'une part mathématiquement,
    en substituant aux méthodes d'inversion exactes de systèmes linéaires 
    des méthodes approchées et itératives. Et d'autre part informatiquement,
    en profilant le code existant pour identifier les goulots d'étranglements,
    puis en [adoptant des constructions Python/NumPy plus efficaces et/ou 
    en introduisant avec Cython du code à la performance comparable au 
    langage C.](http://scipy-lectures.org/advanced/optimizing/index.html)


Technologies
--------------------------------------------------------------------------------

(indicatif)

  - Python, 
  
  - NumPy, 
  
  - Python Imaging Library (PIL/[Pillow](https://pillow.readthedocs.io)),
  
  - [Cython](https://cython.org/).



Références
--------------------------------------------------------------------------------

  - [**Poisson image editing.** P. Pérez, M. Gangnet, A. Blake. 
    ACM Transactions on Graphics (SIGGRAPH'03), 22(3):313-318, 2003.](http://www.irisa.fr/vista/Papers/2003_siggraph_perez.pdf)

  - [**The GIMP Documentation.** Paint Tools : Heal.](https://docs.gimp.org/en/gimp-tool-heal.html)

  - [**De la photographie numérique à la photographie computationnelle.** F. Sur.
    Mines Nancy & Loria, Séance 11. "Édition d'images par l'équation de Poisson"](https://members.loria.fr/FSur/enseignement/photo/seance11_4pp.pdf).

  - [**Complex Analysis and Applications.** S. Boisgérault. MINES ParisTech. Atelier "Poisson Image Editing"](http://eul.ink/complex-analysis/Poisson%20Image%20Editing/).

