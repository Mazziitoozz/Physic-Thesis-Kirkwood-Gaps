# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:58:05 2019

@author: Mazziitoozz
"""
'''
Metodo de Rungekutta4

Funcion que nos vale para calcular la posicion y la velocidad de un objeto acelerado en funcion del tiempo
 Input:
         a =     aceleracion que sufre el cuerpo
         r0 =    vector que contenga posicion inicial
         v0 =    vector que contenga la velocidad inicial
         dt =    paso de tiempo
         tend =  tiempo final
     
    Output:
        x_vector, y_vector, z_vector =      Vectores que contienen las posiciones del cuerpo en funcion del tiempo 
        vx_vector, vy_vector, vz_vector =   Vectores que contienen las velocidades del cuerpo en funcion del tiempo 
        t_vector =                          Vector que contiene los tiempos

Ejemplo de funcion
 def a(x,y,z):
    ax= -G*M*x/(x**2+y**2+z**2)**(3/2)
    ay= -G*M*y/(x**2+y**2+z**2)**(3/2)
    az= -G*M*z/(x**2+y**2+z**2)**(3/2)
    return [ax,ay,az]
'''
def RungeK_4(a,r0,v0,dt,tend):

#Creamos vectores de las posiciones, tiempo y velocidades
    
    x_vector = []
    y_vector = []
    z_vector = []
    
    t_vector = []
    
    vx_vector = []
    vy_vector = []
    vz_vector = []
    
#Condiciones iniciales

    x = r0[0]
    y = r0[1]
    z = r0[2]
    t=0         #Tiempo a partir del cual empezamos a contar
    vx = v0[0]
    vy = v0[1]
    vz = v0[2]
   
#Decimos que el primer elemento de nuestros vectores sea:
   
    x_vector.append(x)
    y_vector.append(y)
    z_vector.append(z)
    
    vx_vector.append(vx)
    vy_vector.append(vy)
    vz_vector.append(vz)

    t_vector.append(t)
    
    n=int(tend/dt)      #Numero de elementos que contendran nuestros vectores

    for i in range (0,n):

#Las  k de las velocidades que las denotaremos como k1vx,k1vy,k1vz
#Las k para las posiciones las denotaremos como k1x, k1y,k1z

#Ecuaciones Rungekutta4

        [k1vx, k1vy, k1vz] = a(x, y, z)

        k1x = vx    
        k1y = vy
        k1z = vz

        [k2vx, k2vy, k2vz] = a(x + k1x * (dt / 2), y + k1y * (dt / 2), z + k1z * (dt / 2))

        k2x = vx + k1vx * (dt / 2)
        k2y = vy + k1vy * (dt / 2)
        k2z = vz + k1vz * (dt / 2)

        [k3vx, k3vy, k3vz] = a(x + k2x * (dt / 2), y + k2y * (dt / 2), z + k2z * (dt / 2))

        k3x = vx + k2vx * (dt / 2)
        k3y = vy + k2vy * (dt / 2)
        k3z = vz + k2vz * (dt / 2)

        [k4vx, k4vy, k4vz] = a(x + k3x * dt, y + k3y * dt, z + k3z * dt)

        k4x = vx + k3vx * dt
        k4y = vy + k3vy * dt
        k4z = vz + k3vz * dt

#Finalmente obtenemos las velocidades y posiciones siguientes

        vx_next = vx + (dt / 6) * (k1vx + 2 * k2vx + 2 * k3vx + k4vx)
        vy_next = vy + (dt / 6) * (k1vy + 2 * k2vy + 2 * k3vy + k4vy)
        vz_next = vz + (dt / 6) * (k1vz + 2 * k2vz + 2 * k3vz + k4vz)

        x_next = x + (dt / 6) * (k1x + 2 * k2x + 2 * k3x + k4x)
        y_next = y + (dt / 6) * (k1y + 2 * k2y + 2 * k3y + k4y)
        z_next = z + (dt / 6) * (k1z + 2 * k2z + 2 * k3z + k4z)
        
         
        x_vector.append(x_next)             # Guardamos los valores en nuestros vectores
        y_vector.append(y_next)
        z_vector.append(z_next)
    
        vx_vector.append(vx_next)
        vy_vector.append(vy_next)
        vz_vector.append(vz_next)
        
        t_next = t + dt
        
        t_vector.append(t_next)
    
        x = x_next                      # Actualizamos los valores  para realizar de nuevo el bucle
        y = y_next
        z = z_next
        
        t = t_next
        
        vx = vx_next
        vy = vy_next
        vz = vz_next
        
    return t_vector,x_vector, y_vector, z_vector, vx_vector, vy_vector, vz_vector