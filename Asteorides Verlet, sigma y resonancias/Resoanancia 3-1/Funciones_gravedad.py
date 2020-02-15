# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:04:55 2019

@author: Mazziitoozz
"""

'''FUNCIONES DE LA GRAVEDAD'''

from math import sin,cos,pi,sqrt,exp

#Calculo la interaccion entre el asteoride y Jupiter 
def grav_sun_Jupiter(xa,ya,za, xj,yj,zj): #Podriamos generalizarla si quisieramos, poniendo Mjup y Msun como imput
    Mjup=1.898E27
    Msun=1.989E30

    raj=sqrt((xa-xj)**(2)+(ya-yj)**(2)+(za-zj)**(2))   # Distancia de Jupiter
    ra=( xa ** 2 + ya ** 2 + za ** 2 ) ** (1/2)     # Distancia del asteoride
   
    ax= -4 * pi ** 2 * xa / ra ** 3 - 4 * pi ** 2 * (Mjup/Msun) * (xa-xj)/raj**3 #Aceleracion debida al sol y a jupiter
    ay= -4 * pi ** 2 * ya / ra ** 3 - 4 * pi ** 2 * (Mjup/Msun) * (ya-yj)/raj**3
    az= -4 * pi ** 2 * za / ra ** 3 - 4 * pi ** 2 * (Mjup/Msun) * (za-zj)/raj**3
    return [ax,ay,az]

#Calculo primero las posiciones de Jupiter
def grav_sun(x,y,z):
    ax= -4 * pi ** 2 * x / ( x ** 2 + y ** 2 + z ** 2 ) ** (3/2)
    ay= -4 * pi ** 2 * y / ( x ** 2 + y ** 2 + z ** 2 ) ** (3/2)
    az= -4 * pi ** 2 * z / ( x ** 2 + y ** 2 + z ** 2 ) ** (3/2)
    return [ax,ay,az]
