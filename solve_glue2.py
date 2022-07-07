
import numpy as np
import matplotlib.pyplot as plt
import logging
import scipy.sparse as sc
from scipy.sparse.linalg import spsolve
from PIL import Image, ImageTk
import tkinter as tk

from base_objects import lapAfinal, make_b

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 850



def solve2():
   fig, axes = plt.subplots(6, figsize = (10,60))
   #the first two plots are source then target
   """m est le nombre de lignes de la matrice rognée, n est le nombre de colonnes"""

   target = Image.open('images/objects-final.jpeg').resize((SCREEN_WIDTH,SCREEN_HEIGHT))
   source = Image.open("images/objects-final.jpeg").resize((SCREEN_WIDTH,SCREEN_HEIGHT))
   source_pos,target_pos = tkinter_img_large(source,target) #[x1,y1,x2,y2], [x1,y1]
   print("sourcepos", source_pos)
   print("target_pos", target_pos)
   if not source_pos:
      raise Exception('tkinter did not receive source image from user')

   source = source.crop(source_pos)
   print(f"working with source shape : ", source.size)
   source = np.asarray(source)
   m,n = source.shape[:2]
   source_dict = {'Reds':source[::,::,0], 'Greens' :source[::,::,1],'Blues': source[::,::,2] }
   
   #make target rectangle of the same size as source
   
   target_x,target_y =  target_pos
   target = target.crop((target_x,target_y, target_x+n, target_y+m))
   target=np.asarray(target)
   target_dict = {'Reds':target[::,::,0], 'Greens' :target[::,::,1],'Blues': target[::,::,2] }

   #testing with just the grey version #[0.2989, 0.5870, 0.1140]
   axes[0].imshow(source,vmin = 0, vmax = 255)
   axes[1].imshow(target,vmin = 0, vmax = 255)
   #testing with all three versions 
   
   final_arr = np.empty(shape = (m,n,3))
   for i,c in enumerate(source_dict.keys()):
      source = source_dict[c]
      target = target_dict[c]
      source = source.flatten()
      target = target.flatten() 

      #A = lapAfinal2(m,n) 
      A = lapAfinal2(m,n)
      b = make_b2(m,n,source,target)
      print(f"A.shape", A.shape)
      print(f"b.shape", b.shape)
      x = sc.linalg.spsolve(A,b)
      x = rebuild_u(x,target.flatten(),m,n)
      x[x<0] = 0
      x[x>255] = 255
      axes[i+2].imshow(x.astype('uint8'), cmap = c, vmin = 0, vmax = 255)
      final_arr[::,::,i] = x
   final_arr = final_arr.astype('uint8')


   final_img = Image.fromarray(final_arr)
   target = Image.open('images/objects-final.jpeg').resize((SCREEN_WIDTH,SCREEN_HEIGHT))
   target.paste(final_img,(target_x,target_y))
   target.show()
   axes[5].imshow(target)



solve2()

