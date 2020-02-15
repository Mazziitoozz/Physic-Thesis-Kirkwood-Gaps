# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:09:32 2019

@author: Mazziitoozz
"""


import numpy as np
from math import sin,cos,pi,sqrt,exp,fabs
import matplotlib.pyplot as plt
from pylab import plot,title,xlabel,ylabel,legend,figure,show,subplot
from timeit import default_timer as timer
import statistics as stats

from Funciones_gravedad import grav_sun,grav_sun_Jupiter
from Metodo_Verlet import Verlet, Verlet2

#Definimos constantes
tend=1000

deltat=0.01         #year
M_jup= 1.898e27                   #kg
Msun=1.989e30
#Parametros iniciales Jupiter
y0_jup=0
z0_jup=0
exce_jupiter= 0
x0_jup= (1+exce_jupiter) * 5.20     #Distancia al fooco
r0_jup=[x0_jup , 0, 0]
#Velocidades
vx0_jup=0
vy0_jup= sqrt(4 * pi ** 2 * (1-exce_jupiter) / x0_jup * (1+M_jup/Msun))
vz0_jup=0
v0_jup=[vx0_jup, vy0_jup, vz0_jup]

#Asteoride 1
#Posicion
x0_ast1=3
y0_ast1=0
z0_ast1=0
r0_ast1=[x0_ast1 , 0, 0]

#Velocidades 
vx0_ast1=0
vy0_ast1=sqrt(4 * pi ** 2 / abs(x0_ast1 ))  #AU/year
vz0_ast1=0
v0_ast1=[vx0_ast1, vy0_ast1, vz0_ast1]

#Asteoride 2
#Posicion
x0_ast2=3.276
y0_ast2=0
z0_ast2=0
r0_ast2=[x0_ast2 , 0, 0]

#Velocidades 
vx0_ast2=0
vy0_ast2=sqrt(4 * pi ** 2 / abs(x0_ast2 ))   #AU/year
vz0_ast2=0
v0_ast2=[vx0_ast2, vy0_ast2, vz0_ast2]

#Asteoride 3
#Posicion
x0_ast3=3.6  
y0_ast3=0
z0_ast3=0
r0_ast3=[x0_ast3 , 0, 0]

#Velocidades 
vx0_ast3=0
vy0_ast3=sqrt(4 * pi ** 2 / abs(x0_ast3) )  #AU/year
vz0_ast3=0
v0_ast3=[vx0_ast3, vy0_ast3, vz0_ast3]
print(vy0_ast3)

t_jup_V, x_jup_V, y_jup_V, z_jup_V, vx_jup_V, vy_jup_V, vz_jup_V = Verlet (grav_sun , r0_jup, v0_jup, deltat,tend) 

#Calculo las trayectorias de los 3 asteorides
t_ast1_V, x_ast1_V, y_ast1_V, z_ast1_V, vx_ast1_V, vy_ast1_V, vz_ast1_V = Verlet2 (grav_sun_Jupiter , r0_ast1, v0_ast1, deltat,tend,x_jup_V, y_jup_V, z_jup_V)
t_ast2_V, x_ast2_V, y_ast2_V, z_ast2_V, vx_ast2_V, vy_ast2_V, vz_ast2_V = Verlet2 (grav_sun_Jupiter , r0_ast2, v0_ast2, deltat,tend,x_jup_V, y_jup_V, z_jup_V) 
t_ast3_V, x_ast3_V, y_ast3_V, z_ast3_V, vx_ast3_V, vy_ast3_V, vz_ast3_V = Verlet2 (grav_sun_Jupiter , r0_ast3, v0_ast3, deltat,tend,x_jup_V, y_jup_V, z_jup_V)  

#Representamos 10 orbitas 
n=int(tend/deltat)

x2a=[]
y2a=[]
for i in range (10):
    x2a.append(x_ast2_V[9996*i:9996*i+595])
    y2a.append(y_ast2_V[9996*i:9996*i+595])

figure(9)
plt.plot(x_jup_V, y_jup_V,'black',label='Verlet Velocity Jupiter')
plt.plot(x2a,y2a,'b.')

#Distancia al Sol con el paso del Tiempo
x1=np.array(x_ast1_V,float)
y1=np.array(y_ast1_V,float)
r_sun1=(x1**2+y1**2)**(1/2)

x2=np.array(x_ast2_V,float)
y2=np.array(y_ast2_V,float)
r_sun2=(x2**2+y2**2)**(1/2)
x3=np.array(x_ast3_V,float)
y3=np.array(y_ast3_V,float)
r_sun3=(x3**2+y3**2)**(1/2)

xj=np.array(x_jup_V,float)
yj=np.array(y_jup_V,float)
r_sunj=(xj**2+yj**2)**(1/2)

figure(1)
plt.plot(t_jup_V,r_sunj,'black',label='jup')
plt.plot(t_jup_V,r_sun1,'r',label='Ast.1')
plt.plot(t_ast2_V,r_sun2,'b',label='Ast.2')
plt.plot(t_ast3_V,r_sun3,'g',label='Ast.3')
plt.ylabel('Distancia Sol (AU)')
plt.xlabel('Tiempo (años)')
plt.legend( loc = 'upper right')

figure(2)
plt.plot(t_ast2_V,r_sun2,'b',label='Ast.2')
plt.legend( loc = 'upper right')

figure(3)
#plt.plot(t_jup_V,r_sunj,'black',label='jup')
plt.plot(t_ast3_V,r_sun3,'g',label='Ast.3')
plt.legend( loc = 'upper right')

#Orbita de los 3 asteroides
figure(4)

plt.plot(x_jup_V, y_jup_V,'black',label='Verlet Velocity Jupiter')
plt.plot(x_ast1_V, y_ast1_V,'r',label='Asteoride 1')
plt.plot(x_ast2_V, y_ast2_V,'b',label='Asteoride 2')
plt.plot(x_ast3_V, y_ast3_V,'g',label='Asteoride 3')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')

plt.legend( loc = 'upper right')

figure(5)

plt.plot(x_jup_V, y_jup_V,'black',label='Verlet Velocity Jupiter')
plt.plot(x_ast2_V, y_ast2_V,'b',label='Asteoride 2')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')

plt.legend( loc = 'upper right')

figure(6)

plt.plot(x_jup_V, y_jup_V,'black',label='Verlet Velocity Jupiter')
plt.plot(x_ast3_V, y_ast3_V,'g',label='Asteoride 3')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')

plt.legend( loc = 'upper right')

show()

'''
n=int(tend/deltat)
rmaxV=[]
timea=[]
rmaxV1=[]
for i in range(0,n):
    if r_sun1[i]>r_sun1[i-1] and r_sun1[i]>r_sun1[i+1]:   
       rmaxV.append(r_sun1[i])
       timea.append(i)
    if r_sun3[i]>r_sun3[i-1] and r_sun3[i]>r_sun3[i+1]:   
       rmaxV1.append(r_sun3[i])
'''
