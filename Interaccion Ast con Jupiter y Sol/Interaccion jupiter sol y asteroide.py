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

from Funciones_gravedad import grav_sun,grav_sun_Jupiter,energy_mecanica
from Metodo_Verlet import Verlet, Verlet2
from Metodo_Euler_Cromer import Euler_Cromer,Euler_Cromer2
from Metodo_Rungekutta_4 import RungeK_42,RungeK_4

#Definimos constantes
tend=2000
deltat=0.002         #year
M_jup= 1.898e27                     #kg
Msun=1.989e30
#Parametros iniciales Jupiter
y0_jup=0
z0_jup=0
exce_jupiter=0.048
x0_jup= (1+exce_jupiter) * 5.20      #Distancia al fooco
r0_jup=[x0_jup , 0, 0]
#Velocidades
vx0_jup=0
vy0_jup= sqrt(4 * pi ** 2 * (1-exce_jupiter) / x0_jup * (1+M_jup/Msun))
vz0_jup=0
v0_jup=[vx0_jup, vy0_jup, vz0_jup]

#Asteoride Juno
#Posicion
exce_ast=0.2554
x0_ast1=3.353	
y0_ast1=0
z0_ast1=0
r0_ast1=[x0_ast1 , 0, 0]

#Velocidades 

vx0_ast1=0
vy0_ast1=sqrt(4 * pi ** 2 * (1-exce_ast) / x0_ast1 )  #AU/year
vz0_ast1=0
v0_ast1=[vx0_ast1, vy0_ast1, vz0_ast1]

#Calculo primero las posiciones de Jupiter

start2=timer()
t_jup_EC, x_jup_EC, y_jup_EC, z_jup_EC, vx_jup_EC, vy_jup_EC, vz_jup_EC =\
    Euler_Cromer (grav_sun , r0_jup, v0_jup, deltat,tend) 
start3=timer()
t_jup_V, x_jup_V, y_jup_V, z_jup_V, vx_jup_V, vy_jup_V, vz_jup_V =\
    Verlet (grav_sun , r0_jup, v0_jup, deltat,tend) 
start4=timer()
t_jup_RK4, x_jup_RK4, y_jup_RK4, z_jup_RK4, vx_jup_RK4, vy_jup_RK4, vz_jup_RK4 =\
    RungeK_4 (grav_sun , r0_jup, v0_jup, deltat,tend) 

#Calculo las del asteoride
t_ast1_EC, x_ast1_EC, y_ast1_EC, z_ast1_EC, vx_ast1_EC, vy_ast1_EC, vz_ast1_EC =\
    Euler_Cromer2 (grav_sun_Jupiter , r0_ast1, v0_ast1, deltat,tend,x_jup_EC, y_jup_EC, z_jup_EC) 
end2=timer()

t_ast_V, x_ast1_V, y_ast1_V, z_ast1_V, vx_ast1_V, vy_ast1_V, vz_ast1_V =\
    Verlet2 (grav_sun_Jupiter , r0_ast1, v0_ast1, deltat,tend,x_jup_V, y_jup_V, z_jup_V) 
end3=timer()

t_ast1_RK4, x_ast1_RK4, y_ast1_RK4, z_ast1_RK4, vx_ast1_RK4, vy_ast1_RK4, vz_ast1_RK4 =\
    RungeK_42 (grav_sun_Jupiter , r0_ast1, v0_ast1, deltat,tend,x_jup_RK4, y_jup_RK4, z_jup_RK4) 
end4=timer()

#Calculamos los tiempos de ejecucion y hacemos las gráficas
print('El metodo de Euler Cromer tarda en calcular la trayectoria',end2-start2, 's')
print('El metodo de Verlet tarda en calcular la trayectoria',end3-start3, 's')
print('El metodo de Rungekutta4 tarda en calcular la trayectoria',end4-start4, 's')

figure (1)
plt.plot(x_jup_V, y_jup_V,'black',label='Verlet Velocity Jupiter')

plt.plot(3.353,0,'+m',linewidth=50,label='Afelio de Juno')
plt.plot(-1.988,0,'+g',linewidth=50,label='Perielio de Juno')
plt.plot(x_ast1_EC,y_ast1_EC,'b', label='Euler Cromer ')
plt.plot(x_ast1_V, y_ast1_V,'r',label='Verlet Velocity')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')

plt.legend( loc = 'upper right')
show()

#%% Comparacion de los metodos en el afelio

n=int(tend/deltat)

#Convertimos en vectores las listas de Verlet
x1=np.array(x_ast1_V,float)
y1=np.array(y_ast1_V,float)
r_afel=(x1**2+y1**2)**(1/2)

#Convertimos en vectores las listas de Euler Cromer
x2=np.array(x_ast1_EC,float)
y2=np.array(y_ast1_EC,float)
r_afel2=(x2**2+y2**2)**(1/2)
#Convertimos en vectores las listas de RK4
x3=np.array(x_ast1_RK4,float)
y3=np.array(y_ast1_RK4,float)
r_afel3=(x3**2+y3**2)**(1/2)

#Hacemos el bucle para hallar el afelio
rmaxV=[]
rmaxEC=[]
rmaxRK4=[]

for i in range(0,n):
    if r_afel[i]>r_afel[i-1] and r_afel[i]>r_afel[i+1]:   
       rmaxV.append(r_afel[i])
    if r_afel2[i]>r_afel2[i-1] and r_afel2[i]>r_afel2[i+1]:   
       rmaxEC.append(r_afel2[i])
    if r_afel3[i]>r_afel3[i-1] and r_afel3[i]>r_afel3[i+1]:   
       rmaxRK4.append(r_afel3[i])

#Los convertimos en vectores  para poder aplicar las funciones mean y stdev
rV=np.array(rmaxV,float)
rEC=np.array(rmaxEC,float)
rRK4=np.array(rmaxRK4,float)

#Calculamos las desviaciones
print('La media con Verlet es=',rV.mean())
print('La desviacion respecto al valor real',stats.stdev(rV))                   
print('La media con Euler Cromer es=',rEC.mean())
print('La desviacion respecto al valor real',stats.stdev(rEC)) 

print('La media con RK4 es=',rRK4.mean())
print('La desviacion respecto al valor real',stats.stdev(rRK4)) 


#Pintamos los valores en una recta

a=[stats.stdev(rV),stats.stdev(rV)]
b=[stats.stdev(rEC),stats.stdev(rEC)]
c=[stats.stdev(rRK4),stats.stdev(rRK4)]

d=[0,1]
figure(2)
plt.plot( d,b,'g', label='Euler Cromer ')
plt.plot(d,a,'y', label='Verlet Velocity')
plt.plot( d,c,'r', label='RungeK_4')
plt.ylabel('Desviacion(UA)')
plt.plot(d,[0,0],'b',label='Valor observado')

plt.legend(loc='center') 
show()

#%% Energias
M_ast=2.67*10**19

Ecin_ast_V,Egrav_ast_V,Emec_ast_V= energy_mecanica(x_ast1_V, y_ast1_V, z_ast1_V,\
                 vx_ast1_V, vy_ast1_V, vz_ast1_V,x_jup_V, y_jup_V, z_jup_V, M_ast)
figure(3)

plt.plot(t_jup_V,Emec_ast_V,'red',label='Mecanica')
plt.plot(t_jup_V,Ecin_ast_V,'g',label='Cinetica ')
plt.plot(t_jup_V,Egrav_ast_V,'b',label='Gravitatoria ')
plt.xlabel('Time(year)')
plt.ylabel('Energia mecanica')
title('Verlet')
plt.legend(loc='upper right')

show()



#%%