import numpy as np 
import matplotlib.pyplot as plt
from numpy import asarray
from PIL import Image

img = Image.open('images/objects.jpeg')

def RGB_to_GREY(img):
    im_mat = asarray(img)
    im_grey = im_mat.mean(axis = 2).reshape((-1,1))
    im_grey.reshape((img.height, img.width, -1))
    return im_grey

ara = RGB_to_GREY(img)
plt.imshow(ara)