# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:43:23 2019

@author: Mazziitoozz
"""

'''
Metodo de Verlet 

Funcion que nos vale para calcular la posicion y la velocidad de un objeto acelerado en funcion del tiempo. Metodo de Verlet
    Input:
         a=     aceleracion que sufre el cuerpo
         r0=    vector que contenga posicion inicial
         v0=    vector que contenga la velocidad inicial
         dt=    paso de tiempo
         tend=  tiempo final
     
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

def Verlet(a,r0,v0,dt,tend):
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
        
        [ax, ay, az] = a(x, y, z)     #Aceleracion
    
        x_next= x + vx * dt + 0.5 * ax * dt ** 2    
        y_next= y + vy * dt + 0.5 * ay * dt ** 2    
        z_next= z + vz * dt + 0.5 * az * dt ** 2
        
        [ax_next, ay_next, az_next] = a(x_next, y_next, z_next) # Aceleraciones del paso siguiente
    
        vx_next = vx + 0.5 * ( ax + ax_next ) * dt  # La velocidad del paso siguiente = a la v del paso actual 
        vy_next = vy + 0.5 * ( ay + ay_next ) * dt  # + 0.5 de la suma de la aceleracion actual mas la aceleracion siguiente
        vz_next = vz + 0.5 * ( az + az_next ) * dt
        
        x_vector.append(x_next)      # Guardamos los valores en nuestros vectores
        y_vector.append(y_next)
        z_vector.append(z_next)
    
        vx_vector.append(vx_next)
        vy_vector.append(vy_next)
        vz_vector.append(vz_next)
        
        t_next = t + dt
       
        t_vector.append(t_next)
    
        x = x_next      # Actualizamos los valores  para realizar de nuevo el bucle
        y = y_next
        z = z_next
        
        t = t_next
        
        vx = vx_next
        vy = vy_next
        vz = vz_next
        
    return t_vector,x_vector, y_vector, z_vector, vx_vector, vy_vector, vz_vector

def Verlet2(a,r0,v0,dt,tend,x_jup, y_jup ,z_jup):
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
        
# _next significa del paso siguiente y si no lleva nada significa que es el actual     
        
        [ax, ay, az] = a(x, y, z,x_jup[i], y_jup[i] ,z_jup[i])     #Decimos que esos valores son los de la funcion aceleracion previamente creada
    
        x_next= x + vx * dt + 0.5 * ax * dt ** 2    
        y_next= y + vy * dt + 0.5 * ay * dt ** 2    
        z_next= z + vz * dt + 0.5 * az * dt ** 2
        
        [ax_next, ay_next, az_next] = a(x_next, y_next, z_next, x_jup[i], y_jup[i] ,z_jup[i]) # Definimos las aceleraciones del paso siguiente
    
        vx_next = vx + 0.5 * ( ax + ax_next ) * dt  # La velocidad del paso siguiente = a la v del paso actual 
        vy_next = vy + 0.5 * ( ay + ay_next ) * dt  # + 0.5 de la suma de la aceleracion actual mas la aceleracion siguiente
        vz_next = vz + 0.5 * ( az + az_next ) * dt
        
        x_vector.append(x_next)      # Guardamos los valores en nuestros vectores
        y_vector.append(y_next)
        z_vector.append(z_next)
    
        vx_vector.append(vx_next)
        vy_vector.append(vy_next)
        vz_vector.append(vz_next)
#        
        t_next = t + dt
#        
        t_vector.append(t_next)
    
        x = x_next      # Actualizamos los valores  para realizar de nuevo el bucle
        y = y_next
        z = z_next
        
        t = t_next
        
        vx = vx_next
        vy = vy_next
        vz = vz_next
        
    return t_vector,x_vector, y_vector, z_vector, vx_vector, vy_vector, vz_vector     

def Verlet3(a,r0,v0,dt,tend,x_jup , y_jup ,z_jup, x_mar, y_mar, z_mar ):
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
        
        [ax, ay, az] = a(x, y, z,x_jup[i], y_jup[i] ,z_jup[i],x_mar[i], y_mar[i] ,z_mar[i])     #Aceleraciones
    
        x_next= x + vx * dt + 0.5 * ax * dt ** 2    
        y_next= y + vy * dt + 0.5 * ay * dt ** 2    
        z_next= z + vz * dt + 0.5 * az * dt ** 2
        
        [ax_next, ay_next, az_next] = a(x_next, y_next, z_next, x_jup[i], y_jup[i] ,z_jup[i],x_mar[i], y_mar[i] ,z_mar[i]) # Aceleraciones del paso siguiente
    
        vx_next = vx + 0.5 * ( ax + ax_next ) * dt  # La velocidad del paso siguiente = a la v del paso actual 
        vy_next = vy + 0.5 * ( ay + ay_next ) * dt  # + 0.5 de la suma de la aceleracion actual mas la aceleracion siguiente
        vz_next = vz + 0.5 * ( az + az_next ) * dt
        
        x_vector.append(x_next)      # Guardamos los valores en nuestros vectores
        y_vector.append(y_next)
        z_vector.append(z_next)
    
        vx_vector.append(vx_next)
        vy_vector.append(vy_next)
        vz_vector.append(vz_next)
#        
        t_next = t + dt
#        
        t_vector.append(t_next)
    
        x = x_next      # Actualizamos los valores  para realizar de nuevo el bucle
        y = y_next
        z = z_next
        
        t = t_next
        
        vx = vx_next
        vy = vy_next
        vz = vz_next
        
    return t_vector,x_vector, y_vector, z_vector, vx_vector, vy_vector, vz_vector     
