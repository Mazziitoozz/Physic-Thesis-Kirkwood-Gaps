
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:51:25 2019

@author: Mazziitoozz
"""
import random
import numpy as np
from math import sin,cos,pi,sqrt,exp,fabs
import matplotlib.pyplot as plt
from pylab import figure
from Funciones_gravedad import grav_sun,grav_sun_Jupiter
from Metodo_Verlet import Verlet, Verlet2
''' Queremos ver donde acaban los asteorides al cabo del tiempo. Para ello estudiaremos la posicion inicial de los asteroides y su posicion final.De esta manera veremos que cuando estan en resonancia, el radio de su orbita varia considerablemente'''

#Definimos constantes
tend=1000                         # Tiempo a estudiar, ir variando.
deltat=0.05                       # year
M_jup= 1.898e27                   # kg
Msun=1.989e30

#Parametros iniciales Jupiter

exce_jupiter= 0.048
x0_jup= (1+exce_jupiter) * 5.20     #Distancia al fooco
r0_jup=[x0_jup , 0, 0]

#Velocidades
vy0_jup= sqrt(4 * pi ** 2 * (1-exce_jupiter) / x0_jup * (1+M_jup/Msun))
v0_jup=[0, vy0_jup, 0]

#Calculo la trayectoria de Jupiter
t_jup , x_jup , y_jup , z_jup , vx_jup , vy_jup , vz_jup  = Verlet (grav_sun , r0_jup, v0_jup, deltat,tend) 

Initial_position = {}
Final_position = {}
#Hacer 10 veces el bucle
f=open('histogramas 1000 0.05 1000 .txt','w')
for j in range (10):                # numero de simulaciones
    for i in range(1000):           # numero de asteorides, ir variando

        radius = random.uniform(2.48,2.52)      # radio de donde impiezan los asteorides
        
        V_i = sqrt(4 * pi ** 2 / (radius))   
        Init_pos = [radius, 0, 0]
        V_init = [0, V_i, 0]
            
        Initial_position[i] = Init_pos
        
        t_ast, x_ast, y_ast, z_ast, vx_ast, vy_ast, vz_ast =\
        Verlet2 (grav_sun_Jupiter , Init_pos , V_init, deltat,tend,x_jup , y_jup , z_jup )
        
        x_ast = np.array(x_ast,float)
        y_ast = np.array(y_ast,float)
        r_ast = ( x_ast**2 + y_ast**2 ) ** (1/2)
        
        Final_position[i] = [x_ast[-1], y_ast[-1], z_ast[-1], r_ast[-1]]
        
        f.write(str(radius))
        f.write(' ')
        f.write(str(r_ast[-1]))
            
        f.write('\n')
    f.close()  
    hist_vec_init = []
    hist_vec_final = []
    
    for asteroid in Final_position:
        hist_vec_final.append(Final_position[asteroid][3])
        
    for asteroid in Initial_position:
        hist_vec_init.append(Initial_position[asteroid][0])
    
figure(1)
plt.hist(hist_vec_init,50,(2.48,2.54))
plt.xlabel('AU')
plt.ylabel('Numero de asteroides')

figure(2)
plt.hist(hist_vec_final,50,(2.2,2.7))
plt.xlabel('AU')
plt.ylabel('Numero de asteroides')   
    
plt.show()  
 