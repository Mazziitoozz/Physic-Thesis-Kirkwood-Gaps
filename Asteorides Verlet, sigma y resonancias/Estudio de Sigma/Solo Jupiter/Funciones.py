# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:04:55 2019

@author: Mazziitoozz
"""

'''FUNCIONES DE LA GRAVEDAD'''

from math import sin,cos,pi,sqrt,exp
import numpy as np

'''FUNCIONES DE LA GRAVEDAD'''
#Gravedad que sufre el cuerpo celeste debido al Sol

def grav_sun(x,y,z):
    ax= -4 * pi ** 2 * x / ( x ** 2 + y ** 2 + z ** 2 ) ** (3/2)
    ay= -4 * pi ** 2 * y / ( x ** 2 + y ** 2 + z ** 2 ) ** (3/2)
    az= -4 * pi ** 2 * z / ( x ** 2 + y ** 2 + z ** 2 ) ** (3/2)
    return [ax,ay,az]

#Gravedad que sufre el cuerpo celeste debido al Sol y Jupiter

def grav_sun_Jupiter(xa,ya,za, xj,yj,zj): #Podriamos generalizarla si quisieramos, poniendo Mjup y Msun como imput
    Mjup=1.898E27
    Msun=1.989E30

    raj=sqrt((xa-xj)**(2)+(ya-yj)**(2)+(za-zj)**(2))    # Distancia a Jupiter
    ra=( xa ** 2 + ya ** 2 + za ** 2 ) ** (1/2)         # Distancia al Sol
   
    ax= -4 * pi ** 2 * xa / ra ** 3 - 4 * pi ** 2 * (Mjup/Msun) * (xa-xj)/raj**3 #Aceleracion debida al sol y a jupiter
    ay= -4 * pi ** 2 * ya / ra ** 3 - 4 * pi ** 2 * (Mjup/Msun) * (ya-yj)/raj**3
    az= -4 * pi ** 2 * za / ra ** 3 - 4 * pi ** 2 * (Mjup/Msun) * (za-zj)/raj**3
    return [ax,ay,az]

#Gravedad que sufre el cuerpo celeste debido al Sol, Jupiter y otro planeta

def grav_sun_Jupiter_Marte(xa,ya,za, xj,yj,zj,xm,ym,zm): #Podriamos generalizarla si quisieramos, poniendo Mjup y Msun como imput
    Mjup=1.898E27
    Msun=1.989E30
    Mmar=6.415E23 #En este caso es la masa de Marte, pero podria ser la de otro planeta
    
    ram=sqrt((xa-xm)**(2)+(ya-ym)**(2)+(za-zm)**(2))    # Distancia a Marte
    raj=sqrt((xa-xj)**(2)+(ya-yj)**(2)+(za-zj)**(2))    # Distancia a Jupiter
    ra=( xa ** 2 + ya ** 2 + za ** 2 ) ** (1/2)         # Distancia al Sol
 
    #Aceleracion debida al Sol, Jupiter y Marte
    ax= -4 * pi ** 2 * xa / ra ** 3 - 4 * pi ** 2 * (Mjup/Msun) * (xa-xj)/raj**3 - 4 * pi ** 2 * (Mmar/Msun) * (xa-xm)/ram**3 
    ay= -4 * pi ** 2 * ya / ra ** 3 - 4 * pi ** 2 * (Mjup/Msun) * (ya-yj)/raj**3 - 4 * pi ** 2 * (Mmar/Msun) * (ya-ym)/ram**3 
    az= -4 * pi ** 2 * za / ra ** 3 - 4 * pi ** 2 * (Mjup/Msun) * (za-zj)/raj**3 - 4 * pi ** 2 * (Mmar/Msun) * (za-zm)/ram**3 
    return [ax,ay,az]

'''FUNCIONES DE ENERGIA'''
#Energia mecanica teniendo en cuenta la interaccion con el Sol
def energy_mecanica_S(x,y,z,vx,vy,vz,Mplaneta1,Msun):  
    n=np.size(vx)
    Energia_cinet=np.zeros(n)
    Energia_grav=np.zeros(n)
    Energia_mec=np.zeros(n)
    v=np.zeros(n)
    r=np.zeros(n)
    for i in range(n): 
        v[i] =sqrt( vx[i] ** 2 + vy[i] ** 2 + vz[i] ** 2) 
        Energia_cinet[i]= 0.5*v[i] ** 2 * Mplaneta1
        r[i] =sqrt( x[i] ** 2 + y[i] ** 2 + z[i] ** 2)
        Energia_grav[i] = - 4*pi**2*Mplaneta1/ r[i]
        Energia_mec[i]= Energia_grav[i] + Energia_cinet[i]
    return np.array(Energia_cinet), np.array(Energia_grav),np.array(Energia_mec)

#Energia mecanica teniendo en cuenta la interaccion con el Sol y Jupiter
def energy_mecanica(x,y,z,vx,vy,vz,xj,yj,zj,Masteroide):  
    n=np.size(vx)
    Mjup=1.898E27
    Msun=1.989E30
    Energia_cinet=np.zeros(n)
    Energia_grav=np.zeros(n)
    Energia_mec=np.zeros(n)
    v=np.zeros(n)
    rast=np.zeros(n)  
    rajup=np.zeros(n)
    for i in range(n):
        v[i] =sqrt( vx[i] ** 2 + vy[i] ** 2 + vz[i] ** 2) 
        Energia_cinet[i]= 0.5 *v[i] ** 2 * Masteroide
        rast[i] =sqrt( x[i] ** 2 + y[i] ** 2 + z[i] ** 2)
        rajup[i] =sqrt( (x[i]-xj[i]) ** 2 + (y[i]-yj[i]) ** 2 + (z[i]-zj[i]) ** 2)
        
        Energia_grav[i] = - 4*pi**2*Masteroide/ rast[i]  - 4 * pi**2 *(Mjup/Msun)*Masteroide /rajup[i]
        Energia_mec[i]= Energia_grav[i] + Energia_cinet[i]
    return np.array(Energia_cinet), np.array(Energia_grav),np.array(Energia_mec)



