import time
import os
import random
import math
print('Bienvenido al sistema de ubicación para zonas públicas WIFI')

usuario = '51672'
contrasena = '27615'

user_atttempt = input('Ingrese su usuario: ')
if (user_atttempt == "Tripulante2022"):
    print("Este fue mi primer programa y vamos por más")
    exit()
if (usuario != user_atttempt):
    print('Error')
    exit()
password_attempt = input('Ingrese su contraseña: ')
if (contrasena != password_attempt):
    print('Error')
    exit()

add_end = int(usuario[2:5])
operation_list = [6 + 1, 5 + 2, 5 + 2 * 1]
add_end2 = random.choice(operation_list)

catcha_attempt = int(
    input(f'Por favor responda a la respuesta correcta del siguiente catcha de seguridad: {add_end} + {add_end2} : '))

if (catcha_attempt != (add_end + add_end2)):
    print('Error')
else:
    print('Sesión iniciada')

menu_options = ['1. Cambiar contraseña',
                '2. Ingresar coordenadas actuales',
                '3. Ubicar zona wifi más cercana',
                '4. Guardar archivo con ubicación cercana',
                '5. Actualizar registros de zonas wifi desde archivo',
                '6. Elegir opción de menú favorita',
                '7. Cerrar sesión'
                ]


# error_counter = 0
list_of_coordenates = []
predifList = [
    [1.811, -75.820, 58],
    [1.919, -75.843, 1290],
    [1.875, -75.877, 110],
    [1.938, -75.764, 114]
]

R = 6372.795477598

exampleChoice = None
newOrder = None
destination = None
informacion = None
longi = None
lati = None

def newAddres(i):
    latitude = float(input("digite su latitud"))
    if latitude >= 1.740 and latitude <= 1.998:
        pass
    else:
        print("Error coordenada")
        time.sleep(2)
        exit()
    longitude = float(input("digite su longitud"))
    if longitude >= -75.950 and longitude <= -75.689:
        pass
    else:
        print("Error coordenada")
        time.sleep(2)
        exit()

    list_of_coordenates[i-1] = [latitude, longitude]
currentPos = None

def setNewPassword(newPass):
    global contrasena
    contrasena = newPass


def byDistance(list):
    return list[3]


def byConections(list):
    return list[2]

def main():
    global R
    global predifList
    global contrasena
    global newOrder
    global currentPos
    global destination
    global informacion
    global longi
    global lati
    global exampleChoice

    for option in menu_options:
        print(option)

    user_choice = int(input('Elija una opción: '))
    if user_choice == 1:
        while True:
            confirmation = input("Ingrese su contraseña actual")
            if confirmation == contrasena:
                new_password = input("Ingrese su nueva contraseña")
                if new_password != contrasena:
                    setNewPassword(new_password)
                    main()
                else:
                    print("Error")
                    exit()
            else:
                print("Error")
                exit()

    elif user_choice == 2:
        coordenates_counter = 0
         ##sacar de While

        if len(list_of_coordenates) == 0:  # Sinllenar
            while coordenates_counter < 3:
                latitude = float(input("digite su latitud"))
                if latitude >= 1.740 and latitude <= 1.998:
                    pass
                else:
                    print("Error coordenada")
                    time.sleep(2)
                    exit()
                longitude = float(input("digite su longitud"))
                if longitude >= -75.950 and longitude <= -75.689:
                    pass
                else:
                    print("Error coordenada")
                    time.sleep(2)
                    exit()
                list_of_coordenates.append([latitude, longitude])
                coordenates_counter += 1
        else:  # YaLlenado  INDEXAR MÄS
            print(list_of_coordenates)
            mostEast = []
            for i in range(0, 3):
                mostEast.append(list_of_coordenates[i][1])

            print(mostEast)
            northest = max(mostEast)
            if northest == list_of_coordenates[0][1]:
                print(f'La coordenada 1 es la que esta más al oriente')
            elif northest == list_of_coordenates[1][1]:
                print(f'La coordenada 2 es la que esta más al oriente')
            elif northest == list_of_coordenates[2][1]:
                print(f'La coordenada 3 es la que esta más al oriente')

            mostWest = []
            for i in range(0, 3):
                mostWest.append(list_of_coordenates[i][1])

            westEst = min(mostWest)
            if westEst == list_of_coordenates[0][1]:
                print(f'La coordenada 1 es la que esta más al occidente')
            elif westEst == list_of_coordenates[1][1]:
                print(f'La coordenada 2 es la que esta más al occidente')
            elif westEst == list_of_coordenates[2][1]:
                print(f'La coordenada 3 es la que esta más al occidente')

            # actualizar:
            updateCoor = int(
                input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú"))
            if updateCoor == 1:
                newAddres(updateCoor)
            elif updateCoor == 2:
                newAddres(updateCoor)
            elif updateCoor == 3:
                newAddres(updateCoor)
            elif updateCoor == 0:
                main()
            else:
                print("Error actualización")
                time.sleep(2)
                exit()

        main()
    elif user_choice == 3:

        if len(list_of_coordenates) > 0:
            currentPos = int(input("Por favor elija su ubicación actual (1,2 ó 3)"))
            if currentPos == 1:
                exampleChoice = list_of_coordenates[currentPos-1]
            elif currentPos == 2:
                exampleChoice = list_of_coordenates[currentPos - 1]
            elif currentPos == 3:
                exampleChoice = list_of_coordenates[currentPos - 1]
            else:
                print("Error ubicación")
                time.sleep(2)
                exit()
        else:
            print("Error sin registro de coordenadas")
            time.sleep(2)
            exit()

        for i in predifList:
            diffDist = 2 * R * math.asin(math.sqrt(
                (math.sin((i[0] - exampleChoice[0]) / 2)) ** 2 + math.cos(exampleChoice[0]) * math.cos(i[0]) * (
                    math.sin(i[1] - exampleChoice[1] / 2)) ** 2))
            i.append(diffDist)

        predifList.sort(key=byDistance)
        newOrder = predifList[1:3]
        newOrder.sort(key=byConections)
        for i in newOrder:
            print(i)

        indications = int(input("Elija 1 o 2 para recibir indicaciones de llegada"))

        if indications == 1:
            if newOrder[0][1] > exampleChoice[1]:
                longi = "oriente"
            else:
                longi = "occidente"
            if newOrder[0][0] > exampleChoice[0]:
                lati = "norte"
            else:
                lati = "sur"

            print(f"Para llegar a la zona wifi dirigirse primero al {longi} y luego hacia el {lati}")
            print(f"-Tiempo en bus {(newOrder[0][3]/16.67)}")
            print(f"-Tiempo en auto {(newOrder[0][3]/20.83)}")
        elif indications == 2:
            if newOrder[1][1] > exampleChoice[1]:
                longi = "oriente"
            else:
                longi = "occidente"
            if newOrder[1][0] > exampleChoice[0]:
                lati = "norte"
            else:
                lati = "sur"

            print(f"Para llegar a la zona wifi dirigirse primero al {longi} y luego hacia el {lati}")
            print(f"-Tiempo en bus {newOrder[1][3]/16.67}")
            print(f"-Tiempo en auto {newOrder[1][3]/20.83}")
        else:
            print("Error zona wifi")
            exit()
        exitInput = int(input("Presione 0 para salir"))
        if exitInput == 0 :
            main()
        if indications == 1 or indications ==2:
            destination = newOrder[indications-1]
    elif user_choice == 4:
        if (len(list_of_coordenates) > 0 and currentPos):
            informacion = {
                "actual": [currentPos],
                "zonawifi1": [destination[1:3]],
                "recorrido": [destination[4]]
            }
        else:
            print("Error de alistamiento")
            time.sleep(2)
            exit()
        print(informacion)
        confirmExport = int(input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal"))
        if confirmExport == 1:
            print("Exportando archivo")
            time.sleep(3)
            exit()
        elif confirmExport == 0:
            main()
    elif user_choice == 5:
        #archivoExterno = open()
        #archivoExterno.readline()
        updateChoice = int(input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal"))
        if updateChoice == 0:
            main()
    elif user_choice == 7:
        print('Hasta pronto')
        exit()
    elif user_choice == 6:
        user_favorite = int(input('Seleccione opción favorita: '))  # por Ahora solo el 6
        if user_favorite < 1 or user_favorite > 5:  # CORREGIR, ACEPTA FUERA DEL 1 Y 5
            print('Error')
            exit()
        advinanza1 = int(input("¿Qué número viene luego del 6? "))
        if advinanza1 != 7:
            print('Error')
            # error_counter +=1 NO LO RECONOCE
            main()
        else:
            adivinanza2 = int(input("¿Qué número viene luego del 1? "))
            if adivinanza2 != 2:
                print("Error")
                main()
            else:
                temp = menu_options.pop(user_favorite - 1)
                menu_options.insert(0, temp)
                os.system("cls")
                # os.systemclear()
                main()
    elif user_choice == 2021:
        easterEgg = int(input("Dame una latitud y te diré cual hemisferio es…"))
        if easterEgg > 0 :
            print("Usted está en hemisferio norte")
        elif easterEgg < 0 :
            print("Usted está en hemisferio sur")

    elif user_choice == 2022:
        sudAmerica = float(input("Escribe una la coordenada de una longitud en Sudamérica y te diré su huso horario"))
        if sudAmerica >= -81.296 and sudAmerica <= -67.401:
            print("El huso horario es -5")
        elif sudAmerica >= -67.402 and sudAmerica <= -54.316:
            print("El huso horario es -4")
        elif sudAmerica >= -54.316 and sudAmerica <= -35.833:
            print("El huso horario es -3")
    else:
        print("Error")

    # exit()


main()