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

from Funciones_gravedad import grav_sun,grav_sun_Jupiter,grav_sun_Jupiter_Marte
from Metodo_Verlet import Verlet, Verlet2,Verlet3

'''Estudiamos los asteorides en la zona proxima a la resonancia  e incluimos la interaccion con marte'''
#Definimos constantes
tend    =   100000
deltat  =   0.01                        #year
M_jup   =   1.898e27                    #kg
Msun    =   1.989e30                    
M_mar   =   6.415E23
#Parametros iniciales Jupiter

exce_jupiter = 0.048
x0_jup = (1+exce_jupiter) * 5.20     #Distancia al foco
r0_jup = [x0_jup , 0, 0]
#Velocidades
vy0_jup= sqrt(4 * pi ** 2 * (1-exce_jupiter) / x0_jup * (1+M_jup/Msun))
v0_jup=[0, vy0_jup, 0]

#Parametros iniciales Marte
exce_mar=0.093
x0_mar= (1+exce_mar) * 1.52     #Distancia al perihelio
r0_mar=[x0_mar , 0, 0]
#Velocidades
vy0_mar= sqrt(4 * pi ** 2 * (1-exce_mar) / x0_mar * (1+M_mar/Msun))
v0_mar=[0, vy0_mar, 0]

#Calculo primero las posiciones de Jupiter
t_jup, x_jup, y_jup, z_jup, vx_jup, vy_jup, vz_jup =\
Verlet (grav_sun , r0_jup, v0_jup, deltat,tend) 

#Calculo las posiciones de Marte
t_mar, x_mar, y_mar, z_mar, vx_mar, vy_mar, vz_mar = \
Verlet2 (grav_sun_Jupiter ,r0_mar, v0_mar, deltat,tend,x_jup, y_jup, z_jup) 

distancias=[]
semieje=[]
Asteroides=open('Asteorides Marte 100000 0.002.txt','w')

for a in np.arange(2.49,2.53,0.002):
    
    radius = a 
    V_i = sqrt(4 * pi ** 2 / (radius))   
   
    Init_pos = [radius, 0, 0]
    V_init = [0, V_i, 0]
    
    #Calculo las posiciones del asteroide
    t_ast, x_ast, y_ast, z_ast, vx_ast, vy_ast, vz_ast =\
    Verlet3 (grav_sun_Jupiter_Marte , Init_pos, V_init, deltat,tend,x_jup,\
             y_jup, z_jup,x_mar,y_mar,z_mar) 
    
    x_ast = np.array(x_ast,float)
    y_ast = np.array(y_ast,float)
    r_ast = ( x_ast**2 + y_ast**2 ) ** (1/2)
        
    desviacion=abs(max(r_ast)-min(r_ast))
    distancias.append(desviacion)
    semieje.append(radius)
    Asteroides.write(str(desviacion))
    Asteroides.write(' ')
    Asteroides.write(str(radius))
    Asteroides.write('\n')
  
    
Asteroides.close()

'''  
from scipy.optimize import curve_fit 
from scipy import asarray as ar,exp
import statistics as stats 
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