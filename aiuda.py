import simpy
import random
    
#Simulacion de corrida de progamas

#NEW : Se debe esperar que se asigne Ram
#Se va a solicitar la cantidad de memoria (Random)
#Si hay memoria sigue, sino hace cola

#Ready
#1. Debe atender el Cpu
#2. Contador con instrucciones (random)
#3. Cuando se desocupe el cpu puede usarse

#Run
#1. Cpu por tiempo limitado. 3 instrucciones
#2. Actualizar contador. Disminuir las 3 instrucciones
#3. Liberar cpu

#Terminated: No hay mas instrucciones
#Wait: al dejar el CPU se genera un número entero al azar entre 1 y 2.
#Si es 1 entonces pasa a la cola de Waiting para hacer
#operaciones de I/O (entrada/salida). Al dejar esa cola regresa a “ready
#al dejar el CPU y el número generado al azar es 2
#entonces se dirige nuevamente a la cola de “ready”.


#Que necesito? 1. Generar un proceso, 2. Verificar Ram y 3. Verificar Cpu

def proceso(env):
    #Que necesito? numero aleatorio entre 1 y 10
    for x in range(num_procesos):
        yield env.timeout(random.randrange(1,10,1))
        env.process(ram(x,env))
        env.process(cpu(x,env))

def Ram(env):

def cpu(env):
    





