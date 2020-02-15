# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:44:12 2019

@author: Mazziitoozz
"""
import random
import numpy as np
from math import sin,cos,pi,sqrt,exp,fabs
import matplotlib.pyplot as plt
from pylab import figure
from Funciones import grav_sun,grav_sun_Jupiter
from Metodo_Verlet import Verlet, Verlet2 
from scipy import asarray as ar,exp

'''Estudiamos la desviacion de los asteorides desde los radios 2.2,3.45 teniendo en cuenta solo la interaccion con Jupiter. Asumiendo dos casos:Orbita de jupiter es circular o Orbita de Jupiter Eliptica'''

#Definimos constantes
tend    =  1000
deltat  =  0.01                        #year
M_jup   =  1.898e27                     #kg
Msun    =  1.989e30

#Parametros iniciales Jupiter

exce_jupiter=0.048   #Caso eliptico, para caso circular poner excentricidad= 0
x0_jup= (1+exce_jupiter) * 5.20     #Distancia al fooco
r0_jup=[x0_jup , 0, 0]

#Velocidades
vy0_jup= sqrt(4 * pi ** 2 * (1-exce_jupiter) / x0_jup * (1+M_jup/Msun))
v0_jup=[0, vy0_jup, 0]

#Calculo la trayectoria de Jupiter
t_jup , x_jup , y_jup , z_jup , vx_jup , vy_jup , vz_jup  =\
 Verlet (grav_sun , r0_jup, v0_jup, deltat,tend) 

distancias=[]
semieje=[]
Asteroides=open('Asteorides 2.2 3.45 1000 años 0.001 Jupiter eliptico.txt','w')

for radius in np.arange(2.2,3.45,0.001):
     
    V_i = sqrt(4 * pi ** 2 / (radius))   
   
    Init_pos = [radius, 0, 0]
    V_init = [0, V_i, 0]
    
    t_ast, x_ast, y_ast, z_ast, vx_ast, vy_ast, vz_ast =\
    Verlet2 (grav_sun_Jupiter , Init_pos , V_init, deltat,\
             tend,x_jup , y_jup , z_jup )
    
    x_ast = np.array(x_ast,float)
    y_ast = np.array(y_ast,float)
    r_ast = ( x_ast**2 + y_ast**2 ) ** (1/2)
    desviacion=abs(max(r_ast)-min(r_ast))
    
    distancias.append(desviacion)
    semieje.append(radius)
    print(semieje)  
    Asteroides.write(str(desviacion))
    Asteroides.write(' ')
    Asteroides.write(str(radius))
    Asteroides.write('\n')
  
    
Asteroides.close()

'''   
x = ar(semieje)
y = ar(distancias) 

plt.plot(x,y,'b+:',label='data')  
plt.xlabel('Posicion inicial (UA)')
plt.ylabel('Desviacion (UA)')
plt.legend() 
plt.show()
'''

'''
Para escribir
file=open('nombredelarchivo.txt,'w')
file.write(str(x[i]))+ ' ' + str(y[i])
file.write('\n')
file.close()
Para leer
x2=[]
y2=[]
file2= np.loadtxt('ejemplo.txt',delimiter=' ' )  #Pones como estan separados
x2=file2=[:,0]
y2=file2[:,1]
'''