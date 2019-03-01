#===================================================
# Andre Rodriguez
# Sara Zavala 18893
# Hoja de Trabajo 5
# Simulador de procesos, cpu y memoria RAM
# Fecha de entrega 28 de Febrero de 2019
#Estructura de Datos
#===================================================
import simpy
import random

global totalprocesador
def proceso (nombre, env, create_time, procesador,ram):
    global totalprocesador # No es buena práctica pero es necesaría
    global tiempos
    poderprocesador = 3
    estado= "Nuevo"
    # Simular que esta creando el proceso
    yield env.timeout(create_time)

    # Tiempo que tarda en crear el proceso
    creado = env.now

    print(nombre, ": ", estado)
    print('El ', nombre , 'se creo en ', creado)
    # Crear la cantidad de instrucciones a procesar
    instrucciones = random.randint(1, 10)
    # Cantidad de memoria a solicitar
    ramnec = random.randint(1,10)
    print(nombre ,' esta en un estado ', estado ,' contiene ', instrucciones ,' instrucciones a procesar y tardo ',creado,' en crearse')

    with ram.get(ramnec) as encola:
        estado = "ready"
        print(nombre,"Estado: ", estado, "Tiempo: ", env.now) #Tiempo a tener en cuenta
        yield encola #ya esta en la memoria ram
        while instrucciones>2:
            with procesador.request() as proceso:
                yield proceso
                estado = "running"
                instrucciones = instrucciones-poderprocesador
                yield env.timeout(1)
                print(nombre, "Estado: ", estado, "Tiempo: ", env.now) #Tiempo a tener en cuenta
            io = random.randint(1,2)
            if(io == 2):
                yield env.timeout(1)
        if instrucciones<3:
            yield env.timeout(1)
        ram.put(ramnec)


    tiempoTotal = env.now - creado
    tiempos.append(tiempoTotal)
    print('El %s se tardo %f' % (nombre, tiempoTotal))#Tiempo de las gráficas
    totalprocesador = totalprocesador + tiempoTotal


# ----------------------

env = simpy.Environment()  # ambiente de simulación
procesador = simpy.Resource(env, capacity=1)#procesador, modificar capacidad y init
ram = simpy.Container(env, init=100, capacity=100)#RAM, modificar capacidad y init
random.seed(10)  # fijar el inicio de random

totalprocesador = 0
tiempos = list()
cantprocesos = 5 #Cantidad de procesos a realizar
for i in range(cantprocesos):
    env.process(proceso('Proceso %d' % i, env, random.expovariate(1.0 / 10), procesador,ram))

env.run()
desvest = 0
promedio = totalprocesador / cantprocesos
print("El tiempo promedio por proceso es: ", promedio) #Tiempo promedio de cada proceso
for x in tiempos:
    desvest = (x-promedio)*(x-promedio)

desvest = desvest /cantprocesos
print("La desviación estándar de cada proceso es: ", desvest)#Desviación estándar
