#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install galgebra


# In[2]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[3]:


#Imports we will need
import sympy
from galgebra.ga import Ga
from galgebra.printer import latex
from IPython.display import Math

# tell sympy to use our printing by default
sympy.init_printing(latex_printer=latex, use_latex='mathjax')


# In[4]:


from sympy.matrices import Matrix
from sympy import Identity


# In[5]:


#import numpy as np
#import matplotlib.pyplot as plt
#import scipy as sp
#import sympy as smp
#from mpl_toolkits import mplot3d
#from matplotlib import cm


# In[6]:


#from galgebra.ga import Ga
#from galgebra.printer import latex
#from IPython.display import Math


# In[7]:


#G200, e_2 + 2*e_1*e_2, e_1 + 2*e_2, 3*e_1*e_2  = Ga.build('e_2 + 2*e_1*e_2', g=[a, b, c])


# In[8]:


(e_1,e_2)= sympy.symbols('e_1, e_2', real= True)


# In[9]:


a = e_2 + 2*e_1*e_2
b = e_1 + 2*e_2
c = 3*e_1*e_2


# In[12]:


G200 = a*b


# In[14]:


G200


# In[15]:


G200 = b*a


# In[16]:


G200


# In[17]:


G200 = b*a*c


# In[18]:


G200


# In[ ]:




