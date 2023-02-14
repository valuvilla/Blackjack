from ast import main
from random import choice, sample, shuffle
import random


#definimos las posibles respuestas
SI=["si", "S", "s", "Si", "verdadero", "Verdadero", "True", "1"]

#Establecemos el valor y dubujo de cada carta
def diccionario():

    cartas= {
        chr(0x1f0a1): 11,
        chr(0x1f0a2): 2,
        chr(0x1f0a3): 3,
        chr(0x1f0a4): 4,
        chr(0x1f0a5): 5,
        chr(0x1f0a6): 6,
        chr(0x1f0a7): 7,
        chr(0x1f0a8): 8,
        chr(0x1f0a9): 9,
        chr(0x1f0aa): 10,
        chr(0x1f0ab): 10,
        chr(0x1f0ad): 10,
        chr(0x1f0ae): 10,
        }
    
    lista_cartas=list(cartas)
    return lista_cartas, cartas


#Definimos la accion de la banca
def main_banca():
    lista_cartas, cartas = diccionario()
    CARTAS_BANCA = sample(lista_cartas, 2)
    SCORE_BANCA = sum(cartas[carta] for carta in CARTAS_BANCA)
    frase="La banca tenía {} {} y sumaban {}".format(CARTAS_BANCA[0],
                                                          CARTAS_BANCA[1],
                                                          SCORE_BANCA) 
                                                                                                            
    return SCORE_BANCA, frase                                               

#Definimos la accion del jugador
def jugador():
    lista_cartas, cartas =diccionario()
    CARTA_JUGADOR_1=choice(lista_cartas)
    score_jugador_1=cartas[CARTA_JUGADOR_1]
    CARTA_JUGADOR_2=choice(lista_cartas)
    score_jugador_2=cartas[CARTA_JUGADOR_2]
    score=score_jugador_1+score_jugador_2
    carta1_valor1="Su primera carta es {} con un valor de {}".format(CARTA_JUGADOR_1, score_jugador_1)
    return score, score_jugador_1,score_jugador_2, CARTA_JUGADOR_1, CARTA_JUGADOR_2, carta1_valor1

"""
#En caso de plantarse, como se gana
def victoria1():
    SCORE_BANCA, frase = main_banca()
    score_jugador_1, score_jugador_2, CARTA_JUGADOR_1, CARTA_JUGADOR_2, carta1_valor1= jugador()
    print("jugador{}".format(score_jugador_1 + score_jugador_2))
    print("banca{}".format(SCORE_BANCA))
    if SCORE_BANCA < score_jugador_1+score_jugador_2:
            print("El jugador gana")
    if SCORE_BANCA > score_jugador_1+score_jugador_2:
            print("La banca gana")
    return frase

#En caso de seguir, definir la siguiente carta
def tercera_carta():
    lista_cartas, cartas =diccionario()
    score_jugador_1, score_jugador_2, CARTA_JUGADOR_1, CARTA_JUGADOR_2, carta1_valor1 = jugador()
    score=score_jugador_1+score_jugador_2
    carta_jugador_3=choice(lista_cartas)
    score_jugador_3=cartas[carta_jugador_3]
    score_jugador_total=score_jugador_3+score
    print("Sus cartas era {} {} {} y sumaban {}".format(CARTA_JUGADOR_1,CARTA_JUGADOR_2,carta_jugador_3, score_jugador_total))
    return  score_jugador_total

#Como ganar tras seguir

def Victoria2():
    SCORE_BANCA,frase = main_banca()
    score_jugador_total= tercera_carta()
    print(score_jugador_total)
    if SCORE_BANCA<score_jugador_total:
            print("El jugador gana")
    else:
            print("La banca gana")
    return frase
  """  



#Definir una partida
def jugador_simple():
    lista_cartas, cartas =diccionario()
    score, score_jugador_1,score_jugador_2,CARTA_JUGADOR_1, CARTA_JUGADOR_2, carta1_valor1 = jugador()
    print(carta1_valor1)
    SCORE_BANCA, frase = main_banca()
    print("Comprobemos si hay posibilidad de seguir")
    def victoria1():
            if score > 21:
                print("oh no!, parece que se ha pasado \nLa banca gana")
            if SCORE_BANCA < score:
                print("El jugador gana")
            else:
                print("La banca gana")
    if SCORE_BANCA>=17:
        print("No hay posibilidad\nSus cartas eran {} {} y sumaban {}".format(CARTA_JUGADOR_1, CARTA_JUGADOR_2, score))
        print(frase)
        victoria1()
    else:
        def plantarse():
            respuesta=input("Existe posibilidad de seguir\n¿Desea plantarse?\n")
            if respuesta in SI:
                print("Sus cartas eran {} {} y sumaban {}".format(CARTA_JUGADOR_1, CARTA_JUGADOR_2, score))
                print(frase)
                victoria1()
            else:
                def tercera_carta():
                    carta_jugador_3=choice(lista_cartas)
                    score_jugador_3=cartas[carta_jugador_3]
                    score=score_jugador_1+score_jugador_2+score_jugador_3
                    return "Sus cartas era {} {} {} y sumaban {}".format(CARTA_JUGADOR_1,CARTA_JUGADOR_2,carta_jugador_3, score)
                tercera_carta()
                print(frase)
                victoria1()
        plantarse()



#definir el juego con varias partidas
# Funcion que genera un mazo de cartas, que son numeros del 1 al 13, y las baraja.
def generar_mazo() -> list:
    mazo: list = list(range(1,14)) * 4
    shuffle(mazo)
    random.shuffle(mazo)
    return mazo

# Funcion principal del juego. Pide el nombre del jugador, y pregunta si desea jugar.
# Si el jugador responde que si, empieza el juego, y si responde que no, finaliza el juego.
def partida() -> None:
    nombre: str = input("Hola, dime tu nombre: ")
    print("Bienvinid@ al Blackjack, {}".format(nombre))
    partidas: int = 0
    while True:
        pregunta: str = input("¿Desea jugar?\n")
        if pregunta in SI:
            partidas += 1
            jugador_simple()
        else:
            print("FIN DE PARTIDA\n{} ha jugado {} veces".format(nombre,partidas))
            print("hasta luego, {}".format(nombre))
            break


partida()

if __name__=="__main__":
    main()

