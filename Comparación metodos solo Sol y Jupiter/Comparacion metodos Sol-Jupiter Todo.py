# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:11:34 2019

@author: Mazziitoozz
"""
import numpy as np
from math import sin,cos,pi,sqrt,exp,fabs
import matplotlib.pyplot as plt
from pylab import plot,title,xlabel,ylabel,legend,figure,show,subplot,size
from timeit import default_timer as timer
import statistics as stats

from Funciones import grav_sun, energy_mecanica_S
from Metodo_Euler import Euler
from Metodo_Euler_Cromer import Euler_Cromer
from Metodo_Verlet import Verlet
from Metodo_Rungekutta_4 import RungeK_4

#Definimos constantes
tend=200
deltat=0.002         #year
Msun=1.989e30

#Parametros iniciales Jupiter Con el origen en el Sol
y0_jup=0
z0_jup=0
exce_jupiter=0.048
x0_jup= (1+exce_jupiter) * 5.20    #UA
M_jup= 1.898e27                     #kg

vx0_jup=0
vy0_jup= sqrt(4 * pi ** 2 * (1-exce_jupiter) / x0_jup * (1+M_jup/Msun))  #AU/year 
vz0_jup=0

#Posicion de Jupiter
r0_jup=[x0_jup , 0, 0]
v0_jup=[vx0_jup, vy0_jup, vz0_jup]

#LLamamos a las funciones que contienen los metodos de integracion numerica
start1=timer()
t_jup_E, x_jup_E, y_jup_E, z_jup_E, vx_jup_E, vy_jup_E, vz_jup_E = Euler (grav_sun , r0_jup, v0_jup, deltat,tend)  
end1=timer()
start2=timer()
t_jup_EC, x_jup_EC, y_jup_EC, z_jup_EC, vx_jup_EC, vy_jup_EC, vz_jup_EC = Euler_Cromer (grav_sun , r0_jup, v0_jup, deltat,tend) 
end2=timer()
start3=timer()
t_jup_V, x_jup_V, y_jup_V, z_jup_V, vx_jup_V, vy_jup_V, vz_jup_V = Verlet (grav_sun , r0_jup, v0_jup, deltat,tend) 
end3=timer()
start4=timer()
t_jup_RK4, x_jup_RK4, y_jup_RK4, z_jup_RK4, vx_jup_RK4, vy_jup_RK4, vz_jup_RK4 =  RungeK_4 (grav_sun , r0_jup, v0_jup, deltat,tend) 
end4=timer()

#Comparamos los metodos
print('El metodo de Euler tarda en calcular la trayectoria',end1-start1, 's')
print('El metodo de Euler Cromer tarda en calcular la trayectoria',end2-start2, 's')
print('El metodo de Verlet tarda en calcular la trayectoria',end3-start3, 's')
print('El metodo de Rungekutta4 tarda en calcular la trayectoria',end4-start4, 's')

#%%Comparamos los 4 metodos

figure(1)
#Pintamos el afelio y el perihelio
plt.plot(-(1-exce_jupiter) * 5.20 ,0,'+g',linewidth=50,label='Perihelio de Júpiter')	
plt.plot(	(1+exce_jupiter) * 5.20 ,0,'+m',linewidth=50,label='Afelio de Júpiter')
#Pintamos las orbitas
plt.plot(x_jup_E, y_jup_E,'g', label='Euler')
plt.plot(x_jup_EC, y_jup_EC,'y', label='Euler Cromer ')
plt.plot(x_jup_V, y_jup_V,'b', label='Verlet Velocity')
plt.plot(x_jup_RK4, y_jup_RK4,'r', label='RungeK_4')

plt.xlabel('x(AU)')
plt.ylabel('y(AU)')


plt.legend()
plt.legend( loc = 'center')

show()

#%% Calculamos el periodo  y lo comparamos con el valor Real

n=int(tend/deltat)
T1_jup=0
T2_jup=0
T_jup=[]
x_afel=[]
x_afel1=[]
x_afel2=[]
tol=0.00000065
for i in range(0,n):
    if fabs(x_jup_V[i]-x_jup_V[0])<tol:                          #abs
        T1_jup=T2_jup    
        T2_jup = deltat * i
        T_jup1 =T2_jup-T1_jup
        T_jup.append(T_jup1)
        x_afel.append(fabs(x_jup_V[i]-x_jup_V[0]))

    if fabs(x_jup_EC[i]-x_jup_EC[0])<tol:                          #abs
        x_afel1.append(fabs(x_jup_EC[i]-x_jup_EC[0]))     

    if fabs(x_jup_RK4[i]-x_jup_RK4[0])<tol:                          #abs
        x_afel2.append(fabs(x_jup_RK4[i]-x_jup_RK4[0]))    

Tjup=5.204267**(3/2)*2*pi/sqrt(4*pi**2) 
x_afelm=sum(x_afel)/(np.size(x_afel)-1)
x_afel1m=sum(x_afel1)/(np.size(x_afel1)-1)
x_afel2m=sum(x_afel2)/(np.size(x_afel2)-1) #Quitamos el primer elemento porque es un 0

#Perido lo convertimos en lista
T_jupm=sum(T_jup)/(np.size(T_jup)-1)
lista=np.array(T_jup[1:],float)
media=lista.mean()
desviacion=lista.std() 
print('La media es=',media, 'La desviacion es',desviacion,'La varianza es', lista.var())
print('La desviacion respecto al valor real',stats.stdev(lista)) 

print('El periodo real de Jupiter es= ' ,Tjup ,'años') 
print('La desviacion en el afelio con Verlet es=',x_afelm) 
print('La desviacion en el afelio con Euler Cromer es=',x_afel1m) 
print('La desviacion en el afelio con RK4 es=',x_afel2m) 
print('El periodo experimental de jupiter es=',T_jupm)

#Pintamos los valores en una recta
a=[x_afel1m,x_afel1m]
b=[x_afelm,x_afelm]
c=[x_afel2m,x_afel2m]
d=[0,1]
figure(2)
plt.plot( d,a,'y', label='Euler Cromer ')
plt.plot(d,b,'g', label='Verlet Velocity')
plt.plot( d,c,'r', label='RungeK_4')
plt.ylabel('Desviacion (UA)')
plt.plot(d,[0,0],'b',label='Valor observado')

plt.legend(loc='upper right') 
show()



#%% Energias con los distintos metodos

Ecin_jup_E,Egrav_jup_E,Emec_jup_E= energy_mecanica_S(x_jup_E, y_jup_E, z_jup_E, vx_jup_E, vy_jup_E, vz_jup_E, M_jup,Msun)
Ecin_jup_V,Egrav_jup_V,Emec_jup_V= energy_mecanica_S(x_jup_V, y_jup_V, z_jup_V, vx_jup_V, vy_jup_V, vz_jup_V, M_jup,Msun)
Ecin_jup_EC,Egrav_jup_Ec,Emec_jup_EC= energy_mecanica_S(x_jup_EC, y_jup_EC, z_jup_EC, vx_jup_EC, vy_jup_EC, vz_jup_EC , M_jup,Msun)
Ecin_jup_RK4,Egrav_jup_RK4,Emec_jup_RK4= energy_mecanica_S(x_jup_RK4, y_jup_RK4, z_jup_RK4, vx_jup_RK4, vy_jup_RK4, vz_jup_RK4, M_jup,Msun)

figure(3)
plt.plot(t_jup_E,Emec_jup_E,'g',label='Euler ')
plt.plot(t_jup_V,Emec_jup_V,'red',label='Verlet Velocity ')
plt.plot(t_jup_E,Emec_jup_RK4,'pink',label='RK4 ')
plt.plot(t_jup_V,Emec_jup_EC,'black',label='Euler Cromer')
plt.xlabel('Time(años)')
plt.ylabel('Energia mecanica (kg(AU/años)^2)')

plt.legend(loc='upper right')

show()
      