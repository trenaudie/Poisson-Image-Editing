
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import logging
logging.basicConfig(level = logging.INFO, format = "%(threadName)s - %(message)s")


import tkinter as tk
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 850




def tkinter_img_large(img1:Image.Image, img2:Image.Image ):
   assert(img1) #source image but uncropped
   assert(img2) #target image but uncropped
   window = tk.Tk()
   #window.geometry("1700x800")
   window.maxsize(SCREEN_WIDTH,SCREEN_HEIGHT)
   frame0 = tk.Frame(height = 5, bg = "white", master = window)
   frame0.pack()
   label0 = tk.Label(master = frame0, text="Click twice on the image to select a source image")
   label0.pack(side = 'top')
   frame1 = tk.Frame(height=SCREEN_HEIGHT, width=SCREEN_WIDTH, master=window)
   frame1.pack(side='top', fill='both', expand=True)
   img1 = img1.resize((SCREEN_WIDTH,SCREEN_HEIGHT))
   imgtk1= ImageTk.PhotoImage(img1, master = window)
   label1 = tk.Label(frame1, image = imgtk1)
   label1.pack()
   
   window2 = tk.Toplevel(master = window)
   frame02 = tk.Frame(height = 5, bg = "white", master = window2)
   frame02.pack(side='top', fill='both', expand=True)
   label02 = tk.Label(master = frame02, text="Click once on the image to select a destination image")
   label02.pack(side = 'top')
   frame2 = tk.Frame(height=SCREEN_HEIGHT, width=SCREEN_WIDTH, master=window2)
   frame2.pack()
   img2 = img2.resize((SCREEN_WIDTH,SCREEN_HEIGHT))
   imgtk2 =  ImageTk.PhotoImage(img2, master = window2)
   label2 = tk.Label(frame2, image = imgtk2)
   label2.pack()
   window2.maxsize(SCREEN_WIDTH,SCREEN_HEIGHT)
   
   sourcepos = []
   destpos= []
   def dest_handler(event):
      destpos.append(event.x)
      destpos.append(event.y)
      assert(len(destpos) == 2)
      window.destroy()
      

   def source_handler(event):
      sourcepos.append(event.x)
      sourcepos.append(event.y)
      if len(sourcepos) >= 4:
         label0.config(text = 'Thank you. Switch to other window.')
         label1.unbind('<Button-1>')
         label2.bind('<Button-1>',dest_handler)
   
   label1.bind("<Button-1>", source_handler)
   window.mainloop()
            
   if len(destpos) == 2 : 
      return sourcepos,destpos
   else:
      raise TimeoutError('No Location for Destination Detected.')