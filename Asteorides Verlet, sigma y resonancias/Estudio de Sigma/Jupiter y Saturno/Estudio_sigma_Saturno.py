# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:29:23 2019

@author: Mazziitoozz
"""


import random
import numpy as np
from math import sin,cos,pi,sqrt,exp,fabs
import matplotlib.pyplot as plt
from pylab import figure

from Funciones_gravedad import grav_sun,grav_sun_Jupiter,grav_sun_Jupiter_Marte
from Metodo_Verlet import Verlet, Verlet2,Verlet3

#Definimos constantes
tend = 100000
deltat = 0.01                        #year
M_jup = 1.898e27                     #kg
Msun = 1.989e30
M_sat= 5.683E26

#Parametros iniciales Jupiter

exce_jupiter = 0.048
x0_jup = (1+exce_jupiter) * 5.20      #Distancia al afelio
r0_jup = [x0_jup , 0, 0]
#Velocidades
vy0_jup = sqrt(4 * pi ** 2 * (1-exce_jupiter) / x0_jup * (1+M_jup/Msun))
v0_jup = [0, vy0_jup, 0]

#Parametros iniciales Saturno

exce_sat=0.056
x0_sat= (1+exce_sat) * 9.582     #Distancia afelio
r0_sat=[x0_sat , 0, 0]
#Velocidades
vx0_sat=0
vy0_sat= sqrt(4 * pi ** 2 * (1-exce_sat) / x0_sat * (1+M_sat/Msun))
vz0_sat=0
v0_sat=[vx0_sat, vy0_sat, 0]


#Calculo primero las posiciones de Jupiter
t_jup, x_jup, y_jup, z_jup, vx_jup, vy_jup, vz_jup =\
Verlet (grav_sun , r0_jup, v0_jup, deltat,tend) 

#Calculo las posiciones de Saturno
t_sat, x_sat, y_sat, z_sat, vx_sat, vy_sat, vz_sat = \
Verlet2 (grav_sun_Jupiter ,r0_sat, v0_sat, deltat,tend,x_jup, y_jup, z_jup) 

distancias=[]
semieje=[]
Asteroides=open('Asteorides Saturno 3.26 3.45 100000 0.005 .txt','w')

for a in np.arange(3.26,3.43,0.005):
    
    radius = a 
    V_i = sqrt(4 * pi ** 2 / (radius))   
   
    Init_pos = [radius, 0, 0]
    V_init = [0, V_i, 0]
    
    #Calculo las posiciones del asteroide
    t_ast, x_ast, y_ast, z_ast, vx_ast, vy_ast, vz_ast =\
    Verlet3 (grav_sun_Jupiter_Marte , Init_pos, V_init, deltat,tend,\
             x_jup, y_jup,z_jup,x_sat,y_sat,z_sat) 
    
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

from scipy.optimize import curve_fit 
from scipy import asarray as ar,exp
import statistics as stats
print(x)
print(y)
n = len(x)       #the number of data 
mean = sum(x*y)/sum(y)    #note this correction 
sigma = np.sqrt(sum(y*(x-mean)**2)/sum(y))  #note this correction 
print(sigma)
def gaus(x,a,x0,sigma): 
    return a*exp(-(x-x0)**2/(2*sigma**2)) 

popt,pcov = curve_fit(gaus,x,y,p0=[max(y),mean,sigma]) 
print(stats.stdev(semieje))

plt.plot(x,y,'b+:',label='data') 
 # plt.plot(x,gaus(x,*popt),'ro:',label='fit') 
plt.xlabel('Posicion inicial (UA)')
plt.ylabel('Desviacion (UA)')
plt.legend() 
plt.show()
'''

'''
plt.plot(semieje,distancias,'r')
plt.xlabel('semieje')
plt.ylabel('desviacion')
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