#!/usr/bin/env python
# coding: utf-8

# ## Solución al péndulo simple

# En el siguiente Jupyter Notebook se desarrolla un código didáctico para resolver la ecuación de movimiento del péndulo simple y que servirá como actividad con fecha 28-agosto-2020 para la materia Análisis de Datos. 

# La ecuación de movimiento que rige al péndulo simple es: $\ddot\theta+\frac gl\sin\theta=0$. Donde $g$ representa es el valor de la gravedad y $l$ la longitud del péndulo. Dado que es una ecuación diferencial de segundo orden se tiene que especificar las condiciones iniciales: $\theta(0)=\theta_0$ y $\dot\theta(0)={\dot\theta}_0$.

# In[12]:


import numpy as np
import matplotlib.pyplot as plt


# In[13]:


#Declaración de constantes y parámetros del sistema
t0=0
tf=10
n=500
dt=(tf-t0)/n
l=.2
k=-9.81/l


# In[14]:


t=np.arange(t0,tf,dt)
x=np.zeros(n) 
v=np.zeros(n)
#Condiciones iniciales
x[0]=1.57
v[0]=2


# In[15]:


#Iteraciones en las soluciones del sistema en función del tiempo
for i in range(0,n-1):
    k1=dt*v[i]
    l1=dt*(np.sin(x[i]))*k
    k2=dt*(v[i]+l1/2)
    l2=dt*(np.sin(x[i]+k1/2))*k
    k3=dt*(v[i]+l2/2)
    l3=dt*(np.sin(x[i]+k2/2))*k
    k4=dt*(v[i]+l3)
    l4=dt*(np.sin(x[i]+k3))*k
    
    x[i+1]=x[i]+(k1+2*k2+2*k3+k4)/6
    v[i+1]=v[i]+(l1+2*l2+2*l3+l4)/6
print('********************* COMPLETADO :) *******************');


# In[22]:


#Resultados. Gráfica de la posición angular de la masa respecto al tiempo.
fig=plt.figure(1)
ax1=fig.add_subplot(111)
ax1.plot(t,x,color="blue",linewidth=1,linestyle="-",fillstyle="none")    
ax1.set_xlabel("$t$ [s] ",color="blue")        
ax1.set_ylabel("$x$ [rad]",color='b')
plt.show()


# In[23]:


#Resultados. Gráfica de la velocidad angular de la masa respecto al tiempo.
fig=plt.figure(1)
ax1=fig.add_subplot(111)
ax1.plot(t,v,color="red",linewidth=1,linestyle="-",fillstyle="none")    
ax1.set_xlabel("$t$ [s] ",color="red")        
ax1.set_ylabel("$v$ [rad/s]",color='red')
plt.show()


# In[ ]:




