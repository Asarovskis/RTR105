#!/usr/bin/env python
# coding: utf-8

# 
# Laboratorijas darbs - saknes meklēšana.
# 
# Dotā funkcija (1-x)*exp(-x)
# 
# Tiek importēts exp un moduļa rēķināšanas komanda fabs no math
# 
# Tiek importēta aizkavēšanas funkcija sleep no time
# 

# In[1]:


from math import exp, fabs
from time import sleep


# Tiek definēta funkcija f(x)

# In[2]:


def f(x):
    return (1-x)*exp(-x)


# Tiek definēti skaitļi, starp kuriem tiks meklēta sakne

# In[3]:


a = -0.5
b = 3.2


# Tiek aprēķinātas funkcijas vērtības intervāla galapunktos

# In[4]:


funa = f(a)
funb = f(b)


# Tiek noteikts vai šajā intervālā vispār ir saknes

# In[5]:


if (funa * funb > 0.0):
    print("Dotajaa intervaalaa [%s, %s] saknju nav"%(a,b))
    sleep(1); exit()  
else:
    print ("Dotajaa intervaalaa sakne(s) ir!")


# Dotajaa intervaalaa sakne(s) ir!
# 
# Definē precizitāti ar kuru meklēs sakni

# In[6]:


deltax = 0.01


# Tiek noteiktas saknes. Tas tiek noteikts cikliski samazinot robežas līdz galapunktu starpība ir mazāka par deltax(precizitāti). Lai noskaidrotu cik reizes vajag sašaurināt intervālu tiek ieviests mainīgais k un pie katras cikla izpildes tam tiek pieskaitīts 1.
# 
# Argumenta gala vērtība ir abu galapunktu summas dalījums pret 2. Šo vērtibu ievieto dotajā funkcijā. Ja, reizinot to ar funkcijas vērtību intervāla sākumā ir mazāks par 0, tad intervāla galapunkts ir argumenta vērtība. Citādāk sākuma punkts ir argumenta gal vērtība.

# In[7]:


k=0
while (fabs (b-a) > deltax ):
    k=k + 1
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0. ):
        b=x
    else:
        a=x


# Aprēķina funkcijas vērtību pie argumenta vērtības.

# In[8]:


deffunk = (1-x)*exp(-x)


# Izprintē argumenta vērtību, funkcijas vērtību, uz intervāla samazināšanas reižu skaitu.

# In[9]:


print ("Sakne ir: ", x)
print ("Funkcijas vertiiba ir:", deffunk)
print ("Tik reizes vajadzeeja daliit uz puseem", k)
