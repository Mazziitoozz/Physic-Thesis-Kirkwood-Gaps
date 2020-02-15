# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:23:32 2019

@author: Mazziitoozz
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:41:05 2019

@author: Mazziitoozz
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:36:19 2019

@author: Mazziitoozz
"""

import numpy as np
from math import sin,cos,pi,sqrt,exp,fabs
import matplotlib.pyplot as plt
from pylab import plot,title,xlabel,ylabel,legend,figure,show,subplot
from timeit import default_timer as timer
import statistics as stats


from Funciones_gravedad import grav_sun,grav_sun_Jupiter,grav_sun_Jupiter_Marte
from Metodo_Verlet import Verlet, Verlet2,Verlet3

#Definimos constantes
tend = 1000
deltat = 0.01                        #year
M_jup = 1.898e27                     #kg
Msun = 1.989e30
M_sat= 5.683E26

#Parametros iniciales Jupiter

exce_jupiter = 0.048
x0_jup = (1+exce_jupiter) * 5.20      #Distancia al perihelio
r0_jup = [x0_jup , 0, 0]
#Velocidades
vy0_jup = sqrt(4 * pi ** 2 * (1-exce_jupiter) / x0_jup * (1+M_jup/Msun))
v0_jup = [0, vy0_jup, 0]

#Parametros iniciales Saturno

exce_sat=0.056
x0_sat= (1+exce_sat) * 9.582     #Distancia al perihelio
r0_sat=[x0_sat , 0, 0]
#Velocidades
vx0_sat=0
vy0_sat= sqrt(4 * pi ** 2 * (1-exce_sat) / x0_sat * (1+M_sat/Msun))
vz0_sat=0
v0_sat=[vx0_sat, vy0_sat, 0]


#Asteoride Juno
#Posicion

x0_ast1=3.2	

r0_ast1=[x0_ast1 , 0, 0]

#Velocidades 

vx0_ast1=0
vy0_ast1=sqrt((4 * pi ** 2) / x0_ast1 )  #AU/year
vz0_ast1=0
v0_ast1=[vx0_ast1, vy0_ast1, vz0_ast1]

#Calculo primero las posiciones de Jupiter

t_jup, x_jup, y_jup, z_jup, vx_jup, vy_jup, vz_jup =\
Verlet (grav_sun , r0_jup, v0_jup, deltat,tend) 

#Calculo las posiciones de Saturno
t_sat, x_sat, y_sat, z_sat, vx_sat, vy_sat, vz_sat = \
Verlet2 (grav_sun_Jupiter ,r0_sat, v0_sat, deltat,tend,x_jup, y_jup, z_jup) 

#Calculo las posiciones del asteroide
t_ast, x_ast1, y_ast1, z_ast1, vx_ast1, vy_ast1, vz_ast1 =\
Verlet3 (grav_sun_Jupiter_Marte , r0_ast1, v0_ast1, deltat,tend,x_jup, y_jup,\   
z_jup,x_sat,y_sat,z_sat)               # Cambiar en la funcion grav_sun_Jupiter_Marte la Masa del planeta y poner Saturno

plt.plot(x_jup, y_jup,'black',label='Jupiter')

plt.plot(x_ast1,y_ast1,'g',label='Asteroide')
plt.plot(x_sat, y_sat,'r',label='Saturno ')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')

plt.legend( loc = 'upper right')
show()
