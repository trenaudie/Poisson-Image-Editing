from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import logging
logging.basicConfig(level = logging.INFO, format = "%(threadName)s - %(message)s")
import scipy.sparse as sc
from scipy.sparse.linalg import spsolve
import threading
import psutil
import time

import tkinter as tk

img = Image.open("images/objects-final.jpeg")


def tkinter_img(img:Image.Image):
   window = tk.Tk()
   window.maxsize(1200,800)
   window.geometry("1200x1200")
   frame0 = tk.Frame(height = 300, bg = "white")
   frame0.pack()
   label0 = tk.Label(master = frame0, text="Click twice to select a source image")
   label0.pack()


   frame = tk.Frame(height=450, width=350, master=window)
   frame.pack()
   #frame.place(relx =0.1, rely = 0.1)
   img = img.resize((1200,800))
   imgtk = ImageTk.PhotoImage(img)
   label = tk.Label(frame, image = imgtk)
   label.pack()
   sourcepos = []
   destpos= []
   def source_handler(event):
      sourcepos.append(event.y)
      sourcepos.append(event.x)

      print(f"mouse clicked at pos {sourcepos[-2:]}!")
   def dest_handler(event):
      destpos.append(event.y)
      destpos.append(event.x)

      print(f"mouse clicked at pos {destpos[-2:]}!")
   label.bind("<Button-1>", source_handler)

   def thread_function():
      while True:
         if len(sourcepos) == 4:
            label.unbind('<Button-1>')
            newimg = img.crop((sourcepos[1],sourcepos[0], sourcepos[3], sourcepos[2]))
            """for proc in psutil.process_iter():
               if proc.name() == "display":
                  proc.kill() """
            newimg.show()
            label0.configure(text="Click once to select destination position")
            label0.pack()
            label.unbind('<Button-1>')
            label.bind('<Button-1>',dest_handler)
            break
      while True:
         if len(destpos) == 2:
            print("destination position obtained: ", destpos)
            break
            
   t = threading.Thread(target = thread_function  )
   t.start()

   window.mainloop()
   t.join()



tkinter_img(img)