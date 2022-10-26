from ast import main
from random import choice, sample

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



def main_banca():
    lista_cartas, cartas = diccionario()
    cartas_banca = sample(lista_cartas, 2)
    score_banca = sum(cartas[carta] for carta in cartas_banca)
    frase="La banca tenía {} {} y sumaban {}".format(cartas_banca[0],
                                                          cartas_banca[1],
                                                          score_banca)
    return score_banca, frase                                               
    


def jugador_simple():
    lista_cartas, cartas =diccionario()
    carta_jugador_1=choice(lista_cartas)
    score_jugador=cartas[carta_jugador_1]
    print("Su primera carta es {} con un valor de {}".format(carta_jugador_1, score_jugador))
    carta_jugador_2=choice(lista_cartas)
    score_jugador+=cartas[carta_jugador_2]
    score_banca, frase = main_banca()
    if score_banca>=17:
        print(frase)
        if score_banca<score_jugador:
            print("El jugador gana")
        else:
            print("La banca gana")
    else:
        respuesta=input("Existe posibilidad de seguir\n¿Desea plantarse?\n")
        if respuesta in SI:
            print("Sus cartas eran {} {} y sumaban {}".format(carta_jugador_1, carta_jugador_2, score_jugador))
            print(frase)
            if score_banca<score_jugador:
                print("El jugador gana")
            else:
                print("La banca gana")
        else:
            carta_jugador_3=choice(lista_cartas)
            score_jugador+=cartas[carta_jugador_3]
            print("Sus cartas era {} {} {} y sumaban {}".format(carta_jugador_1,carta_jugador_2,carta_jugador_3, score_jugador))
            score_banca, frase = main_banca()
            print(frase)
            if score_jugador > 21:
                print("oh no!, parece que se ha pasado \nLa banca gana")
            else:
                if score_banca<score_jugador:
                    print("El jugador gana")
                else:
                    print("La banca gana")


SI=["si", "S", "s", "Si", "verdadero", "Verdadero", "True", "1"]


def partida():
    nombre=input("Hola, dime tu nombre: ")
    print("Bienvinid@ al Blackjack, {}".format(nombre))
    partidas=0
    while True:
        pregunta=input("¿Desea jugar?\n")
        if pregunta in SI:
            partidas+=1
            jugador_simple()
        else:
            print("FIN DE PARTIDA\n{} ha jugado {} veces".format(nombre,partidas))
            return"hasta luego, {}".format(nombre)
            break

print(partida())

if __name__=="__main__":
    main()

