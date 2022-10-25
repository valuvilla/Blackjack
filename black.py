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
    print("La banca tenía {} {} y sumaban {}".format(cartas_banca[0],
                                                          cartas_banca[1],
                                                          score_banca))
    return score_banca


def jugador():
    lista_cartas, cartas =diccionario()
    carta_jugador_1=choice(lista_cartas)
    score1=cartas[carta_jugador_1]
    print("Su primera carta es {} con un valor de {}".format(carta_jugador_1, score1))
    carta_jugador_2=choice(lista_cartas)
    score2=cartas[carta_jugador_2]
    respuesta=input("¿Desea plantarse?: \n 1.Si \n 2.No \n")
    if respuesta=="1":
        print("comprobemos si ha ganado \n Sus cartas era {} {} y en total sumaban {}".format(carta_jugador_1, carta_jugador_2, score1+score2))
        score_banca = main_banca()
        if int(score1+score2)<score_banca:
            print("La banca gana")
        else:
            print("El jugador gana")
    if respuesta=="2":
        carta_jugador_3=choice(lista_cartas)
        score3=cartas[carta_jugador_3]
        print("sus cartas era {} {} {} y en total sumaban {}".format(carta_jugador_1,carta_jugador_2,carta_jugador_3, score1+score2+score3))
        if int(score1+score2+score3) > 21:
            print("oh no!, parece que se a pasado")
            print("La banca gana")
        else:
            print("comprobemos si ha ganado")
            score_banca = main_banca()
            if int(score1+score2+score3)<score_banca:
                print("La banca gana")
            else:
                print("El jugador gana")




jugador()


