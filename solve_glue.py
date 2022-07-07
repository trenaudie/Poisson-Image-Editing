
#Cette fonction correspond 100% Source
# Lap Sol = Lap Source avec des 1 au niveau du bord



import numpy as np
import matplotlib.pyplot as plt
import logging
import scipy.sparse as sc
from scipy.sparse.linalg import spsolve
from PIL import Image, ImageTk
import tkinter as tk

from base_objects import lapAfinal, make_b

def solve_glue():
   """source = Image.open("images/objects.jpeg")
   source_y,source_x = 1400,1600
   source_width, source_height = 50,200
   source = source.crop((source_x,source_y,source_x+source_width, source_y+source_height)) """
   source = Image.open('figs/possion1.png')
   source = source.crop((270,180,330,300)) #x1,y1,x2,y2
   source = np.asarray(source)
   m,n = source.shape[:2]
   
   source_dict = {'Reds':source[::,::,0], 'Greens' :source[::,::,1],'Blues': source[::,::,2] }
   
   #make target rectangle of the same size as source
   target = Image.open("images/objects-final.jpeg")
   target_x,target_y =  1000,600
   target = target.crop((target_x,target_y, target_x+n, target_y+m))
   target=np.asarray(target)
   target_dict = {'Reds':target[::,::,0], 'Greens' :target[::,::,1],'Blues': target[::,::,2] }


   #testing with all three colors 
   fig, axes = plt.subplots(6, figsize = (10,60))
   #the first two plots are source then target
   axes[0].imshow(source)
   axes[1].imshow(target)
   final_arr = np.empty(shape = (m,n,3))
   for i,c in enumerate(source_dict.keys()):
      source = source_dict[c]
      target = target_dict[c]
      assert(source.ndim == 2 )
      source = source.flatten()
      target = target.flatten() 

      A = lapAfinal(m,n) 
      b = make_b(m,n,source,target)
      u = sc.linalg.spsolve(A,b)
      u = u.reshape((m,n)).astype('uint8')
      """u[u<0] = 0
      u[u>255] = 255 """
      axes[i+2].imshow(u, cmap = c, vmin = 0, vmax = 255)
      final_arr[::,::,i] = u
      final_arr = final_arr.astype('uint8')
   

   


   final_img = Image.fromarray(final_arr)
   target2 = Image.open("images/objects-final.jpeg")
   target2.paste(final_img,(target_x,target_y))
   target2.show()
   axes[5].imshow(target2)


solve_glue()
