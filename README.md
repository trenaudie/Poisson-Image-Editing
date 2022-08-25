# Edition d'images de Poisson
### Poisson Image Editing


![](figs/objects-final.jpeg)

Contexte
--------------------------------------------------------------------------------

The Poisson Image Editing Algorithm alows us to:
- Copy and paste images onto other images with seamless integration (like Photoshop's *Glue*)
- Remove parts of images (like Photoshop's *heal tool*)  

The Algorithm attributes to a given pixel inside the domain the mean of its neighbors. On the boundary, the pixels are given by
the target image.
The solution uses a linear system.

This technique hinges on an implementation of the imaeg as a 2D function u(x,y), and the resolution of the Dirichlet system:
$\Delta u(x,y) = 0$ with boundary conditions.

--------------------------------------------------------------------------------

*Original Image
([Original photo by Vadim Sherbakov](https://unsplash.com/photos/tCICLJ5ktBE), 
[licence Unsplash Creative Commons Zero](https://unsplash.com/license))*

![](figs/objects.jpeg)



Objectives
--------------------------------------------------------------------------------

Implementation of the algorithm.
Improvement of the algorithm:
- using a maxed gradient approach
- using a mixed gradient approach
- using a 2D Fourier approach
- using sparse matrices.

Technologies
--------------------------------------------------------------------------------

  - Python, 
  
  - NumPy, 
  
  - Python Imaging Library (PIL/[Pillow](https://pillow.readthedocs.io)),
  
  
User interface
--------------------------------------------------------------------------------
See file _Interface_utilisateur_. 
You will be redirected to an html page where you will choose one image to glue onto a given background


Project presentation and results 
--------------------------------------------------------------------------------
See *Edition_d_image_de_Poisson.pdf*.
This document presents the theoretical approch, then the numerical implementation of the project, and finally our results

Références
--------------------------------------------------------------------------------

  - [**Poisson image editing.** P. Pérez, M. Gangnet, A. Blake. 
    ACM Transactions on Graphics (SIGGRAPH'03), 22(3):313-318, 2003.](http://www.irisa.fr/vista/Papers/2003_siggraph_perez.pdf)

  - [**The GIMP Documentation.** Paint Tools : Heal.](https://docs.gimp.org/en/gimp-tool-heal.html)

  - [**De la photographie numérique à la photographie computationnelle.** F. Sur.
    Mines Nancy & Loria, Séance 11. "Édition d'images par l'équation de Poisson"](https://members.loria.fr/FSur/enseignement/photo/seance11_4pp.pdf).

  - [**Complex Analysis and Applications.** S. Boisgérault. MINES ParisTech. Atelier "Poisson Image Editing"](http://eul.ink/complex-analysis/Poisson%20Image%20Editing/).

