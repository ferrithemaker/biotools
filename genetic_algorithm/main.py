import random
import string
import sys, pygame
import time


objetivo = "this is a genetic algorithm :)"

pygame.init()
pygame.display.set_caption('surprise surprise')

width = 700
height = 200
size = [width, height]

black = [0, 0, 0]
red = [255,0,0]
green = [0,255,0]

#screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

font = pygame.font.Font('freesansbold.ttf', 64)


GENES = 25
MAX_GENERACION = 30000


class Individuo(object):
    # la clase Individuo solo guarda 2 variables:
    # adn (la cadena original)
    # fitness (la distancia respecto al objetivo)
    def __init__(self, adn, fitness):
        self.adn = adn
        self.fitness = fitness


def calcular_fitness(origen, valor_objetivo):
    # la funcion fitness nos da un valor de "distancia" entre el objetivo
    # y el valor actual, es parecido al "resiudo" de una regresión lineal.
    # contra mayor es el fitness, mas lejos estamos de la solución.
    fitness = 0
    for i in range(0, len(origen)):
        fitness += (ord(valor_objetivo[i]) - ord(origen[i])) ** 2
        # TEST para ejercicio 2
        # fitness += abs(ord(valor_objetivo[i]) - ord(origen[i]))
    return fitness


def mutacion(padre1, padre2):
    # el hijo es como padre1
    adn_hijo = padre1.adn[:]
    # define las posiciones que copiara de padre2
    start = random.randint(0, len(padre2.adn) - 1)
    stop = random.randint(0, len(padre2.adn) - 1)
    if start > stop:
        stop, start = start, stop

    adn_hijo[start:stop] = padre2.adn[start:stop]
    # en adn_hijo tenemos una parte de padre1 y otra sección de padre2
    posicion = random.randint(0, len(adn_hijo) - 1)
    # añadimos la mutación en una posición aleatoria
    adn_hijo[posicion] = chr(ord(adn_hijo[posicion]) + random.randint(-1, 1))
    # calculamos el fitness nuevo y lo devolvemos
    fitness_hijo = calcular_fitness(adn_hijo, objetivo)
    return Individuo(adn_hijo, fitness_hijo)


def padre_al_azar(poblacion):
    # retornamos "individuo" al azar
    return poblacion[int(random.random() * random.random() * (GENES - 1))]


def escribe_generacion(generacion, poblacion):
    # nos muestra la población (que viene ordenada por fitness)
    print('Pasos de simulación: %d' % generacion)
    print()
    print('  Fitness         ADN')
    print('------------------------')
    for candidato in poblacion:
        print("%6i %15s" % (candidato.fitness, ''.join(candidato.adn)))
    print()


def inicializa_poblacion():
    poblacion = []
    # Vamos a generar el conjunto  inicial de genes
    for i in range(0, GENES):
        # string pritable nos devuelve un string con todos los caracteres (-5 del final)
        adn = [random.choice(string.printable[:-5]) for _ in range(0, len(objetivo))]
        # en adn tenemos un valor inicial de lista de caracteres de tamaño len(objetivo)
        # calculamos la distancia respecto al objetivo
        fitness = calcular_fitness(adn, objetivo)
        # Guardamos los generados en una instancia de la clase Individuo
        candidate = Individuo(adn, fitness)
        # Creamos una lista de 'candidatos' (instancias de Individuo)
        poblacion.append(candidate)
    return poblacion


def simulacion():
    # tenemos en población una lista de Individuos (adn y fitness)
    poblacion = inicializa_poblacion()
    generacion = 0
    # vamos a iniciar el sistema de generaciones
    while True and generacion < MAX_GENERACION:
        # eventos de pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # contador de generaciones
        if generacion < MAX_GENERACION and poblacion[0].fitness != 0:
            generacion += 1
            # ordenamos la poblacion por el fitness
            poblacion.sort(key=lambda candidate: candidate.fitness)
            # si el prmer elemento tiene fitness == 0
            # implica que hemos encontrado el resultado correcto
            # escojemos dos padres al azar
            padre1 = padre_al_azar(poblacion)
            padre2 = padre_al_azar(poblacion)
            # creamos un hijo en base a la mezcla de padre1 y padre2
            hijo = mutacion(padre1, padre2)
            # si el hijo mejora el fitness del ultimo elemento, lo sustituimos
            if hijo.fitness < poblacion[-1].fitness:
                poblacion[-1] = hijo
            # en este proceso ira progresivamente mejorando el fitness
            # generar ouput pygame
        screen.fill(black)
        text_gen = font.render("generation " + str(generacion), True, green, black)
        text_fit = font.render("fitness " + str(poblacion[0].fitness), True, green, black)
        text_output = font.render(''.join(poblacion[0].adn), True, green, black)
        text_genRect = text_gen.get_rect()
        text_outputRect = text_gen.get_rect()
        text_fitRect = text_gen.get_rect()
        text_genRect.x = 300
        text_genRect.y = 500
        text_fitRect.x = 300
        text_fitRect.y = 600
        text_outputRect.x = 300
        text_outputRect.y = 300
        screen.blit(text_gen, text_genRect)
        screen.blit(text_output, text_outputRect)
        screen.blit(text_fit, text_fitRect)
        pygame.display.flip()
        time.sleep(0.005)

simulacion()
