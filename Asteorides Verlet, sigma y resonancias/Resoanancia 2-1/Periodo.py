# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 20:24:30 2019

@author: Mazziitoozz
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:50:30 20198

@author: Mazziitoozz
"""

import numpy as np
from math import sin,cos,pi,sqrt,exp,fabs
import matplotlib.pyplot as plt
from pylab import plot,title,xlabel,ylabel,legend,figure,show,subplot


from Funciones_gravedad import grav_sun,grav_sun_Jupiter
from Metodo_Verlet import Verlet, Verlet2
import statistics as stats

#Definimos constantes
tend=500
deltat=0.001         #year
M_jup= 1.898e27                   #kg
Msun=1.989e30

'''Parametros iniciales Jupiter'''
y0_jup=0
z0_jup=0
exce_jupiter=0.048
x0_jup= (1+exce_jupiter) * 5.20     #Distancia al fooco
r0_jup=[x0_jup , 0, 0]
#Velocidades
vx0_jup=0
vy0_jup= sqrt(4 * pi ** 2 * (1-exce_jupiter) / x0_jup * (1+M_jup/Msun))
vz0_jup=0
v0_jup=[vx0_jup, vy0_jup, vz0_jup]

'''Asteorides'''
#Asteoride 1
#Posicion

x0_ast1=2.5

y0_ast1=0
z0_ast1=0
r0_ast1=[x0_ast1 , 0, 0]

#Velocidades 
vx0_ast1=0
vy0_ast1= sqrt(4 * pi ** 2 / abs(x0_ast1 ))  
vz0_ast1=0
v0_ast1=[vx0_ast1, vy0_ast1, vz0_ast1]
print(vy0_ast1)

#%%
#Calculo la trayectoria de Jupiter
t_jup_V, x_jup_V, y_jup_V, z_jup_V, vx_jup_V, vy_jup_V, vz_jup_V = Verlet (grav_sun , r0_jup, v0_jup, deltat,tend) 

#Calculo las trayectorias de los 3 asteorides
t_ast1_V, x_ast1_V, y_ast1_V, z_ast1_V, vx_ast1_V, vy_ast1_V, vz_ast1_V = Verlet2 (grav_sun_Jupiter , r0_ast1, v0_ast1, deltat,tend,x_jup_V, y_jup_V, z_jup_V)
 
#Distancia al Sol con el paso del Tiempo
x1=np.array(x_ast1_V,float)
y1=np.array(y_ast1_V,float)
r_afel=(x1**2+y1**2)**(1/2)

#Distancia de Jupiter al Sol
xj=np.array(x_jup_V,float)
yj=np.array(y_jup_V,float)
r_sunj=(xj**2+yj**2)**(1/2)

#%%Calculamos el periodo  y lo comparamos con el valor Real

n=int(tend/deltat)
T1_ast=0
T2_ast=0
T_ast=[]
x_afel=[]
for i in range(0,n):
    if r_afel[i]>r_afel[i-1] and r_afel[i]>r_afel[i+1]:   
        T1_ast=T2_ast    
        T2_ast = deltat * i
        T_ast1 =T2_ast-T1_ast
        T_ast.append(T_ast1)

       

print (x_afel)


#Perido lo convertimos en lista
T_astm=sum(T_ast)/(np.size(T_ast)-1)
lista=np.array(T_ast[1:],float)
media=lista.mean()
desviacion=lista.std() #para el calculo de la desviación típica, que equivale a la raíz cuadrada de la varianza
print('La media es=',media, 'La desviacion es',desviacion,'La varianza es', lista.var())
print('La desviacion respecto al valor real',stats.stdev(lista)) #Hago la desviacion con respecto al valor real o con respecto a la meda


print('El periodo experimental de jupiter es=',T_astm)

#%%%

'''HACEMOS LAS GRAFICAS'''

figure(1)
#plt.plot(t_jup_V,r_sunj,'black',label='jup')
plt.plot(t_jup_V,r_afel,'r',label='jup')

show()

#Orbita de los 3 asteroides
figure(2)

plt.plot(x_jup_V, y_jup_V,'black',label='Verlet Velocity Jupiter')
plt.plot(x_ast1_V, y_ast1_V,'r',label='Asteoride 1')

plt.xlabel('x(AU)')
plt.ylabel('y(AU)')

plt.legend( loc = 'upper right')

show()
