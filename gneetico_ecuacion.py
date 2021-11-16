import random
import math
from random import sample
'''
max_actitud_actual = 0 #definimos el valor actitud para la maxima actual
largo = 8 #La longitud del material genetico de cada individuo
num = 15#La cantidad de individuos que habra en la poblacion
pressure = 3 #Cuantos individuos se seleccionan para reproduccion. Necesariamente mayor que 2
mutation_chance = 0.1 #La probabilidad de que un individuo mute
  
def individual(min, max):
    """
        Crea un individual
    """
    print([random.randint(min, max) for i in range(largo)], "\n")
    
    return[random.randint(min, max) for i in range(largo)]
  
def crearPoblacion():
    """
        Crea una poblacion nueva de individuos
    """
    return [individual(0,1) for i in range(num)]

def calcularFitness(individual):
    
    #aqui obtengo la decodificacion
    n=0
    for i in range(len(individual)):
        if individual[i] == 1:
            n+=math.pow(2, 7-i)
    #una ves obtenida la decodificacion obtenemos el valor real       
    x=n*2/255-1
    #ahora si hacemos la prueba de actitud... :c
    y=1-math.pow(x,2)
    return y
def torneo(population):
    puntuados = [ (calcularFitness(i), i) for i in population] 
    
    v=sample([x for x in range(0,15)],15)
    group=[]
    max=0
    for i in range(0,5):
        if (puntuados[v[i]][0] > max):
            if i != 0:
                group.pop()
                if(puntuados[v[i]][0] > max):
                    group.append(puntuados[v[i]])
            else:
                if(puntuados[v[i]][0] > max):
                    group.append(puntuados[v[i]])
        max=puntuados[v[i]][0]
    for i in range(6,10):
        if(puntuados[v[i]][0] > max):
            if i!= 6:
                group.pop()
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
            else:
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
        max=puntuados[v[i]][0]
    for i in range(11,15):
        if(puntuados[v[i]][0] > max):
            if i!= 11:
                group.pop()
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
            else:
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
        max=puntuados[v[i]][0]
    print("hola:")
    print(group)
def selection_and_reproduction(population):
    """
        Puntua todos los elementos de la poblacion (population) y se queda9 con los mejores
        guardandolos dentro de 'selected'
        Despues mezcla el material genetico de los elegidos para crear nuevos individuos y
        llenar la poblacion (guardando tambien una copia de los individuos seleccionados sin
        modificar).
  
        Por ultimo muta a los individuos.
  
    """
    puntuados = [ (calcularFitness(i), i) for i in population] 
    
    v=sample([x for x in range(0,15)],15)
    group=[]
    max=0
    for i in range(0,5):
        if (puntuados[v[i]][0] > max):
            if i != 0:
                group.pop()
                if(puntuados[v[i]][0] > max):
                    group.append(puntuados[v[i]])
            else:
                if(puntuados[v[i]][0] > max):
                    group.append(puntuados[v[i]])
        max=puntuados[v[i]][0]
    max=0
    for i in range(6,10):
        if(puntuados[v[i]][0] > max):
            if i!= 6:
                group.pop()
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
            else:
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
        max=puntuados[v[i]][0]
    max=0
    for i in range(11,15):
        if(puntuados[v[i]][0] > max):
            if i!= 11:
                group.pop()
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
            else:
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
        max=puntuados[v[i]][0]
    selected =  group
  
    #Se mezcla el material genetico para crear nuevos individuos
    for i in range(len(population)-pressure):
        punto = random.randint(1,largo-1)  #Se elige un punto para hacer el intercambio
        padre = random.sample(selected, 2) #Se eligen dos padres
          
        population[i][:punto] = padre[0][:punto] #Se mezcla el material genetico de los padres en cada nuevo individuo
        population[i][punto:] = padre[1][punto:]
  
    return population #El array 'population' tiene ahora una nueva poblacion de individuos, que se devuelven
  
def mutation(population):
    """
        Se mutan los individuos al azar. Sin la mutacion de nuevos genes nunca podria
        alcanzarse la solucion.
    """
    for i in range(len(population)-pressure):
        if random.random() <= mutation_chance:#Cada individuo de la poblacion (menos los padres) tienen una probabilidad de mutar
            punto = random.randint(0,largo-1) #Se elgie un punto al azar
            nuevo_valor = random.randint(0,1) #y un nuevo valor para este punto
  
            #Es importante mirar que el nuevo valor no sea igual al viejo
            while nuevo_valor == population[i][punto]:
                nuevo_valor = random.randint(0,1)
  
            #Se aplica la mutacion
            population[i][punto] = nuevo_valor
  
    return population
      
population = crearPoblacion()#Inicializar una poblacion
print("Poblacion Inicial:\n%s"%(population)) #Se muestra la poblacion inicial
torneo(population)
#Se evoluciona la poblacion
for i in range(100):
    population = selection_and_reproduction(population)
    population = mutation(population)
 
print("\nPoblacion Final:\n%s"%population) #Se muestra la poblacion evolucionada
print("\n\n")
'''
v=sample([x for x in range(0,15)],15)
print (v)





import random
import math
from random import sample
  
max_actitud_actual = 0 #definimos el valor actitud para la maxima actual
largo = 8 #La longitud del material genetico de cada individuo
num = 15#La cantidad de individuos que habra en la poblacion
pressure = 3 #Cuantos individuos se seleccionan para reproduccion. Necesariamente mayor que 2
mutation_chance = 0.1 #La probabilidad de que un individuo mute
  
def individual(min, max):
    """
        Crea un individual
    """
    print([random.randint(min, max) for i in range(largo)], "\n")
    
    return[random.randint(min, max) for i in range(largo)]
  
def crearPoblacion():
    """
        Crea una poblacion nueva de individuos
    """
    return [individual(0,1) for i in range(num)]

def calcularFitness(individual):
    
    #aqui obtengo la decodificacion
    n=0
    for i in range(len(individual)):
        if individual[i] == 1:
            n+=math.pow(2, 7-i)
    #una ves obtenida la decodificacion obtenemos el valor real       
    x=n*2/255-1
    #ahora si hacemos la prueba de actitud... :c
    y=1-math.pow(x,2)
    return y

def torneo(population):
    puntuados = [ (calcularFitness(i), i) for i in population] 
    
    v=sample([x for x in range(0,15)],15)#aqui genero una lista de nuemros aleatorio q no se repiten
    #[3, 2, 12, 13, 10,     4, 14, 1, 8, 9,        5, 7, 6, 11, 0] tomare esas pocciciones
    group=[]
    max=0
    for i in range(0,5):
        if (puntuados[v[i]][0] > max):
            if i != 0:
                group.pop()
                if(puntuados[v[i]][0] > max):
                    group.append(puntuados[v[i]])
            else:
                if(puntuados[v[i]][0] > max):
                    group.append(puntuados[v[i]])
        max=puntuados[v[i]][0]
    max=0
    for i in range(6,10):
        if(puntuados[v[i]][0] > max):
            if i!= 6:
                group.pop()
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
            else:
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
        max=puntuados[v[i]][0]
    max=0
    for i in range(11,15):
        if(puntuados[v[i]][0] > max):
            if i!= 11:
                group.pop()
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
            else:
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
        max=puntuados[v[i]][0]
    print("elegidos del torneo")
    print(group)
    return group
def selection_and_reproduction(population):
    """
        Puntua todos los elementos de la poblacion (population) y se queda9 con los mejores
        guardandolos dentro de 'selected'
        Despues mezcla el material genetico de los elegidos para crear nuevos individuos y
        llenar la poblacion (guardando tambien una copia de los individuos seleccionados sin
        modificar).
  
        Por ultimo muta a los individuos.
  
    """
   
    selected = torneo(population) #Esta linea selecciona los 'n' individuos del final, donde n viene dado por 'pressure'
  
  
    #Se mezcla el material genetico para crear nuevos individuos
    for i in range(len(population)-pressure):
        punto = random.randint(1,largo-1)  #Se elige un punto para hacer el intercambio
        padre = random.sample(selected, 2) #Se eligen dos padres
          
        population[i][:punto] = padre[0][:punto] #Se mezcla el material genetico de los padres en cada nuevo individuo
        population[i][punto:] = padre[1][punto:]
  
    return population #El array 'population' tiene ahora una nueva poblacion de individuos, que se devuelven
  
def mutation(population):
    """
        Se mutan los individuos al azar. Sin la mutacion de nuevos genes nunca podria
        alcanzarse la solucion.
    """
    for i in range(len(population)-pressure):
        if random.random() <= mutation_chance:#Cada individuo de la poblacion (menos los padres) tienen una probabilidad de mutar
            punto = random.randint(0,largo-1) #Se elgie un punto al azar
            nuevo_valor = random.randint(0,1) #y un nuevo valor para este punto
  
            #Es importante mirar que el nuevo valor no sea igual al viejo
            while nuevo_valor == population[i][punto]:
                nuevo_valor = random.randint(0,1)
  
            #Se aplica la mutacion
            population[i][punto] = nuevo_valor
  
    return population
      
population = crearPoblacion()#Inicializar una poblacion
print("Poblacion Inicial:\n%s"%(population)) #Se muestra la poblacion inicial
torneo(population)
#Se evoluciona la poblacion
for i in range(120):
    population = selection_and_reproduction(population)
    population = mutation(population)
 
print("\nPoblacion Final:\n%s"%population) #Se muestra la poblacion evolucionada
print("\n\n")

*************************



import random
import math
from random import sample
  
max_actitud_actual = 0 #definimos el valor actitud para la maxima actual
largo = 8 #La longitud del material genetico de cada individuo
num = 15#La cantidad de individuos que habra en la poblacion
pressure = 3 #Cuantos individuos se seleccionan para reproduccion. Necesariamente mayor que 2
mutation_chance = 0.1 #La probabilidad de que un individuo mute
  
def individual(min, max):
    """
        Crea un individual
    """
    print([random.randint(min, max) for i in range(largo)], "\n")
    
    return[random.randint(min, max) for i in range(largo)]
  
def crearPoblacion():
    """
        Crea una poblacion nueva de individuos
    """
    return [individual(0,1) for i in range(num)]

def calcularFitness(individual):
    
    #aqui obtengo la decodificacion
    n=0
    for i in range(len(individual)):
        if individual[i] == 1:
            n+=math.pow(2, 7-i)
    #una ves obtenida la decodificacion obtenemos el valor real       
    x=n*2/255-1
    #ahora si hacemos la prueba de actitud... :c
    y=1-math.pow(x,2)
    return y
def torneo(population):
    puntuados = [ (calcularFitness(i), i) for i in population] 
    
    v=sample([x for x in range(0,15)],15)
    group=[]
    max=0
    for i in range(0,5):
        if (puntuados[v[i]][0] > max):
            if i != 0:
                group.pop()
                if(puntuados[v[i]][0] > max):
                    group.append(puntuados[v[i]])
            else:
                if(puntuados[v[i]][0] > max):
                    group.append(puntuados[v[i]])
        max=puntuados[v[i]][0]
    max=0
    for i in range(6,10):
        if(puntuados[v[i]][0] > max):
            if i!= 6:
                group.pop()
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
            else:
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
        max=puntuados[v[i]][0]
    max=0
    for i in range(11,15):
        if(puntuados[v[i]][0] > max):
            if i!= 11:
                group.pop()
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
            else:
                if (puntuados[v[i]][0] > max):
                        group.append(puntuados[v[i]])
        max=puntuados[v[i]][0]
    print("elegido_del_Torneo")
    print(group)
def selection_and_reproduction(population):
    """
        Puntua todos los elementos de la poblacion (population) y se queda9 con los mejores
        guardandolos dentro de 'selected'
        Despues mezcla el material genetico de los elegidos para crear nuevos individuos y
        llenar la poblacion (guardando tambien una copia de los individuos seleccionados sin
        modificar).
  
        Por ultimo muta a los individuos.
  
    """
    #torneo(population)
    puntuados = [ (calcularFitness(i), i) for i in population] 
    #Calcula el fitness de cada individuo, y lo guarda en pares ordenados de la forma (5 , [1,2,1,1,4,1,8,9,4,1])
    puntuados = [i[1] for i in sorted(puntuados)] 
    #Ordena los pares ordenados y se queda solo con el array de valores
    population = puntuados
    selected =  puntuados[(len(puntuados)-pressure):] #Esta linea selecciona los 'n' individuos del final, donde n viene dado por 'pressure'
  
  
    #Se mezcla el material genetico para crear nuevos individuos
    for i in range(len(population)-pressure):
        punto = random.randint(1,largo-1)  #Se elige un punto para hacer el intercambio
        padre = random.sample(selected, 2) #Se eligen dos padres
          
        population[i][:punto] = padre[0][:punto] #Se mezcla el material genetico de los padres en cada nuevo individuo
        population[i][punto:] = padre[1][punto:]
  
    return population #El array 'population' tiene ahora una nueva poblacion de individuos, que se devuelven
  
def mutation(population):
    """
        Se mutan los individuos al azar. Sin la mutacion de nuevos genes nunca podria
        alcanzarse la solucion.
    """
    for i in range(len(population)-pressure):
        if random.random() <= mutation_chance:#Cada individuo de la poblacion (menos los padres) tienen una probabilidad de mutar
            punto = random.randint(0,largo-1) #Se elgie un punto al azar
            nuevo_valor = random.randint(0,1) #y un nuevo valor para este punto
  
            #Es importante mirar que el nuevo valor no sea igual al viejo
            while nuevo_valor == population[i][punto]:
                nuevo_valor = random.randint(0,1)
  
            #Se aplica la mutacion
            population[i][punto] = nuevo_valor
  
    return population
      
population = crearPoblacion()#Inicializar una poblacion
print("Poblacion Inicial:\n%s"%(population)) #Se muestra la poblacion inicial
#Se evoluciona la poblacion
for i in range(120):
    population = selection_and_reproduction(population)
    population = mutation(population)
 
print("\nPoblacion Final:\n%s"%population) #Se muestra la poblacion evolucionada
print("\n\n")

torneo(population)

def calculaVR(individual):
    
    #aqui obtengo la decodificacion
    n=0
    for i in range(len(individual)):
        if individual[i] == 1:
            n+=math.pow(2, 7-i)
    #una ves obtenida la decodificacion obtenemos el valor real       
    x=n*2/255-1
    #ahora si hacemos la prueba de actitud... :c
    y=1-math