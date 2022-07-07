
import numpy as np
import matplotlib.pyplot as plt
import logging
import scipy.sparse as sc
from scipy.sparse.linalg import spsolve
from PIL import Image, ImageTk
import tkinter as tk



logging.basicConfig(level = logging.INFO, format = "%(threadName)s - %(message)s")


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 850

half_width = SCREEN_WIDTH//2-10
half_height = SCREEN_HEIGHT//2-10



def lapA(m:int ,n:int):
   """Create laplacian operator matrix, without the boundary condition using SPARSE_MATRIX
   Args:
   m : int - height in pixels of D domain
   n : int - width in pixels of D domain"""
   D = sc.lil_matrix((m,m))
   D.setdiag(4)
   D.setdiag(-1,1)
   D.setdiag(-1,-1)
   I = sc.lil_matrix((m,m))
   I.setdiag(1)
   A = sc.lil_matrix((m*n,m*n))
   for k in range(n):
      A[k*m: k*m+m, k*m: k*m+m] = D
   for k in range(n-1):
      A[k*m:k*m+m,k*m+m:k*m+2*m] = -I
   for k in range(n-1):
      A[k*m+m:k*m+2*m,k*m:k*m+m] = -I
   return A

def make_mask(m,n):
   #The mask m will have the same shape as source, (and cropped target) ie D
   #The mask m has a rectangular of 1s, inside a boundary of 0s
   mask = np.ones(shape = (m,n))
   for k in range(2):
      mask[k] = 0
      mask[-(k+1)] = 0
      mask[:, k] = 0
      mask[:, -(k+1)] = 0

   return mask.flatten()

def lapAfinal(m,n):
   mask = make_mask(m,n)
   print(f"mask.shape =  {mask.shape}")
   A = lapA(m,n)
   print(f"A shape = {A.get_shape()}")

   A[mask == 0] = 0
   A[mask==0, mask==0] = 1
   return A.tocsc()

def make_b(m,n,source, target):
   mask = make_mask(m,n)
   print(f"mask shape in make_b {mask.shape}")
   assert(type(source) == np.ndarray and source.ndim <= 2)
   assert(type(target) == np.ndarray and target.ndim <= 2)
   if source.ndim == 2:
      source = source.flatten()
   A = lapAfinal(m,n) #csc matrix
   

   
   logging.info("Calculating A @ source")
   b =A.dot(source)
   b[mask==0] = target[mask==0]
   return b
#TESTING TKINTER WITH A DIFFERENT SIZE IMAGE










## THESE OBJECTS ARE FOR 100% glue 2nd version


def count_neighbors(i,j,m,n):
   ones = np.ones(shape = (m,n))
   xs, ys = np.indices((m,n))
   mask2 = (xs-i)**2 + (ys-j)**2 <= 1
   return ones[mask2].sum() - 1

def make_mask_not_flat(m,n):
   #The mask m will have the same shape as source, (and cropped target) ie D
   #The mask m has a rectangular of 1s, inside a boundary of 0s
   mask = np.ones(shape = (m,n))
   for k in range(2):
      mask[k] = 0
      mask[-(k+1)] = 0
      mask[:, k] = 0
      mask[:, -(k+1)] = 0
   return mask



def make_S(m,n):
   mask = make_mask_not_flat(m,n)
   N1 = mask.sum()
   N= m*n
   S = np.zeros(shape = (int(N1),N))
   k = 0
   for i in range(m):
      for j in range(n):
         if mask[i][j] == 1:
            S[k][i*n+j] = 1
            k += 1
   return S

def make_S_sparse(m,n):
   mask = make_mask_not_flat(m,n)
   N1 = int(mask.sum())
   N= m*n
   S = sc.lil_matrix((N1,N))
   k = 0
   for i in range(m):
      for j in range(n):
         if mask[i,j] == 1:
            S[k,i*n+j] = 1
            k += 1
   return S.tocsc()




def lapA2(m:int ,n:int):
   """Create laplacian operator matrix, without the boundary condition using SPARSE_MATRIX
   Args:
   m : int - height in pixels of D domain
   n : int - width in pixels of D domain"""
   D = sc.lil_matrix((n,n))
   D.setdiag(-4)
   D.setdiag(1,1)
   D.setdiag(1,-1)
   I = sc.lil_matrix((n,n))
   I.setdiag(1)
   A = sc.lil_matrix((m*n,m*n))
   for k in range(m):
      A[k*n: k*n+n, k*n: k*n+n] = D
   """ for k in range(n*m):
      i,j = k//n, k%n
      #A[k,k] = -count_neighbors(i,j,m,n) """

   for k in range(m-1):
      A[k*n:k*n+n,k*n+n:k*n+2*n] = I
   for k in range(m-1):
      A[k*n+n:k*n+2*n,k*n:k*n+n] = I
   return A.tocsc()

def make_mask_not_flat2(m,n):
   #The mask m will have the same shape as source, (and cropped target) ie D
   #The mask m has a rectangular of 1s, inside a boundary of 0s
   mask = np.ones(shape = (m,n))
   for k in range(2):
      mask[k] = 0
      mask[-(k+1)] = 0
      mask[:, k] = 0
      mask[:, -(k+1)] = 0
   return mask

def lapAfinal2(m,n):
   #A2 = S @ A @ S.T
   A = lapA2(m,n)
   S = make_S_sparse(m,n)
   print(f"working with S.shape = {S.shape}")
   A2 =  S.dot(A.dot(S.transpose()))
   return A2

def make_b2(m,n,source, target):
   # S A S^T \mathbf{u} = S A s - S A r
   mask = make_mask_not_flat(m,n)
   assert(mask.ndim == 2)
   #print(f"mask shape in make_b {mask.shape}")
   assert(type(source) == np.ndarray and source.ndim <= 2)
   assert(type(target) == np.ndarray and target.ndim <= 2)

   #build t
   s = source.copy()
   if s.ndim == 2:
      s = s.flatten()
   assert(s.shape == (m*n,))
   
   #build r
   r = target.flatten()
   r[mask.flatten() == 1] = 0


   A = lapA2(m,n)
   S = make_S_sparse(m,n)

   b =S.dot(A.dot(s))-S.dot(A.dot(r))
   #b = A.dot(t) - A.dot(r)
   return b


def rebuild_u(u, target, m,n):
   mask = make_mask_not_flat(m,n)
   
   x = np.zeros(shape = (m,n))

   x[mask == 1] = u
   x[mask == 0] = target[mask.flatten() == 0]
   return x


## ALGO Gradient mix avec combinaison linéaire des laplaciens


def make_b_mix(m,n,source, target, coef_s :float,coef_t:float):
   # S A S^T \mathbf{u} = S A t - S A r
   mask = make_mask_not_flat(m,n)
   assert(mask.ndim == 2)
   #print(f"mask shape in make_b {mask.shape}")
   assert(type(source) == np.ndarray and source.ndim <= 2)
   assert(type(target) == np.ndarray and target.ndim <= 2)

   #build s
   s = source.copy()
   if s.ndim == 2:
      s = s.flatten()
   assert(s.shape == (m*n,))

   t = target.copy()
   if t.ndim == 2:
      t = t.flatten()
   assert(t.shape == (m*n,))

   
   #build r
   r = target.flatten()
   r[mask.flatten() == 1] = 0


   A = lapA2(m,n)
   S = make_S_sparse(m,n)

   b =S.dot(A.dot(s)*coef_s+ A.dot(t)*coef_t)-S.dot(A.dot(r))
   #b = A.dot(t) - A.dot(r)
   return b

## FOR ALGO Gradients 

def makeDx(m,n):
   """Create derivative Dx operator matrix, using sparse matrix library from scipy 
   Args:
   m : int - height in pixels of D domain
   n : int - width in pixels of D domain"""
   Dx = sc.lil_matrix((m*n,m*n))
   Dx.setdiag(-1)
   I = sc.lil_matrix((n,n))
   I.setdiag(1)
   for k in range(m-1):
      Dx[k*n:k*n+n,k*n+n:k*n+2*n] = I
   return Dx.tocsc()

def makeDy(m,n):
   """Create derivative Dx operator matrix, using sparse matrix library from scipy 
   Args:
   m : int - height in pixels of D domain
   n : int - width in pixels of D domain"""
   Dy = sc.lil_matrix((m*n,m*n))
   Dy.setdiag(-1)
   Dy.setdiag(1,1)
   return Dy.tocsc()

def make_b_derivatives(m,n, source, target):
   #classic poisson image blending but with the derivative operators two times over (to create a laplacian by hand and test if the Dx and Dy operators work)

   # reminder: b = S (Dx vx + Dy vy -  A r)

   #build operators Dx, Dy, A
   Dx=makeDx(m,n)
   Dy=makeDy(m,n)
   A = lapA2(m,n)
   mask = make_mask_not_flat(m,n)
   
   assert(mask.ndim == 2)
   assert(type(source) == np.ndarray and source.ndim <= 2)
   assert(type(target) == np.ndarray and target.ndim <= 2)

   #build s and t
   s = source.copy()
   if s.ndim == 2:
      s = s.flatten()
   t = target.copy()
   if t.ndim == 2:
      t = t.flatten()
   assert(t.shape == (m*n,) and s.shape == (m*n,))

   #build r
   r = target.flatten()
   r[mask.flatten() == 1] = 0
   
   #build vx, vy
   vx = Dx.dot(s)
   vy = Dy.dot(s)

   S = make_S_sparse(m,n)
   return S.dot(Dx.dot(vx) + Dy.dot(vy)- A.dot(r))


def make_b_max(m,n,source, target):
   # S A S^T \mathbf{u} = S A t - S A r
   Dx=makeDx(m,n)
   Dy=makeDy(m,n)
   mask = make_mask_not_flat(m,n)
   
   assert(mask.ndim == 2)
   assert(type(source) == np.ndarray and source.ndim <= 2)
   assert(type(target) == np.ndarray and target.ndim <= 2)

   #build s
   s = source.copy()
   if s.ndim == 2:
      s = s.flatten()
   assert(s.shape == (m*n,))

   t = target.copy()
   if t.ndim == 2:
      t = t.flatten()
   assert(t.shape == (m*n,))


   vx = Dx.dot(s)
   vy = Dy.dot(s)
   wx = Dx.dot(t)
   wy = Dy.dot(t)

   v_norm = vx**2+vy**2
   w_norm = wx**2+wy**2
   v_gt_w = v_norm > w_norm
   qx = sc.lil_matrix((m*n,1))
   qx[v_norm > w_norm,0] = vx[v_norm > w_norm]
   qx[v_norm <= w_norm,0] = wx[v_norm <= w_norm]
   qy = sc.lil_matrix((m*n,1))
   qy[v_norm > w_norm,0] = vy[v_norm > w_norm]
   qy[v_norm <= w_norm,0] = wy[v_norm <= w_norm]
   
   #build r
   r = target.flatten()
   r[mask.flatten() == 1] = 0



   A = lapA2(m,n)
   S = make_S_sparse(m,n)
   return S.dot(Dx.dot(qx) + Dy.dot(qy)- A.dot(r).reshape((-1,1)))


##SOLVE DER MIN 




def make_b_min(m,n,source, target):
   # S A S^T \mathbf{u} = S A t - S A r
   Dx=makeDx(m,n)
   Dy=makeDy(m,n)
   mask = make_mask_not_flat(m,n)
   
   assert(mask.ndim == 2)
   assert(type(source) == np.ndarray and source.ndim <= 2)
   assert(type(target) == np.ndarray and target.ndim <= 2)

   #build s
   s = source.copy()
   if s.ndim == 2:
      s = s.flatten()
   assert(s.shape == (m*n,))

   t = target.copy()
   if t.ndim == 2:
      t = t.flatten()
   assert(t.shape == (m*n,))


   vx = Dx.dot(s)
   vy = Dy.dot(s)
   wx = Dx.dot(t)
   wy = Dy.dot(t)

   v_norm = vx**2+vy**2
   w_norm = wx**2+wy**2
   v_gt_w = v_norm > w_norm
   qx = sc.lil_matrix((m*n,1))
   qx[v_norm > w_norm,0] = wx[v_norm > w_norm]
   qx[v_norm <= w_norm,0] = vx[v_norm <= w_norm]
   qy = sc.lil_matrix((m*n,1))
   qy[v_norm > w_norm,0] = wy[v_norm > w_norm]
   qy[v_norm <= w_norm,0] = vy[v_norm <= w_norm]
   

   #build r
   r = target.flatten()
   r[mask.flatten() == 1] = 0



   A = lapA2(m,n)
   S = make_S_sparse(m,n)


   return S.dot(Dx.dot(qx) + Dy.dot(qy)- A.dot(r).reshape((-1,1)))


