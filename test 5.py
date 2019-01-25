import numpy as np
import matplotlib.pyplot as plt

#This fuction gives oyu the percentage of births that were bornin the
#state and the year you ask in Mexico


def percentaje_birth (municipio,año):
    try:
        arch=open('Nacimientos_registrados_2010_2017.csv','r', encoding= "UTF-8")
#We open the file
    except:
        print("Error, file not found")

    else:

        if not año.isdigit():

            print("Error, enter the year")
        if int(año)<2010 or int(año)>2017:
            print("Only birth between 2010 to 2017 are avalible")

        pos_año=(int(año)-2009)*6-5
        lineas=[]
        for linea in arch:
            lineaP=linea
#First we find the line with the year that we are requiring and then we find the state
            l=lineaP.split(",")
            if l[0] == municipio:
                lista=l
                porcentaje=float(((int(lista[pos_año+1])+int(lista[pos_año+2]))/int(lista[pos_año]))*100)
            else:
                print("State not found")
        return porcentaje

#This fuctions gives you the year that the state you say had less teen pregnancy 

def menorAñosMadresAdolecentes (municipio):
    archivo= open('Nacimientos_registrados_2010_2017.csv')
    años=archivo.readline().split(",")

    #We open the file and we read line by line and we create a list of each line
    linea=archivo.readline().split(",")
    while linea[0]!= municipio:

    #If in the position of the state is the same of the sate it give you error and it end
        #the circle of the while
        linea=archivo.readline().split(",")
        if linea == ['']:
            print("State not found")
            return
        #We start reading line by line and if the fuction is over reading everyline
        #and the state was not found then it give you an error
    minAño = años[1].split()[1]
    minNiños = int(linea[2]) + int(linea[3])
    #We do 2 mins to make comparations the data in the lists
    for i in range(1,8):
        #Since we use the first year that we have the data as the min we not have to
        #iterate between de 0,8
        año = años[1+6*i].split()[1]
        #We use the i to iterate and grab different years and kids
        niños = int(linea[2+6*i]) + int(linea[3+6*i])
        if niños < minNiños:
            minNiños = niños
            minAño = año
            #If they are minor we use the same data
    return minAño


#

def madres_menores_2015 (municipio):
    try:
        arch=open('Nacimientos_registrados_2010_2017.csv','r', encoding= "UTF-8")
        arch2=open('Poblacion_edad_sexo_2015.csv','r', encoding="UTF-8")
    except:
        print("Error, file not found")
    cont=0
    lista_principal=[]

    for linea in arch:
        lineaP=linea
        l=lineaP.split(",")
        lista_principal.append(l)






        cont=cont+1
        pos=0
        if l[0] == municipio:
            num_nacimientos_15_19=int(l[32])

            pos=cont-1

            if pos >= 0 and pos < 10:
                municipio2="00" + str(pos) + " " + municipio

            elif pos >= 10 and pos < 100:
                municipio2="0" + str(pos) + " " + municipio

            elif pos >= 100:
                municipio2= str(pos) + " " + municipio


            listaA=[]
            for linea2 in arch2:
                lineaP2=linea2
                l2=lineaP2.split(",")
                listaA.append(l2)

                #Ya que municipio2 esta listo para usarse, necesitamos que cuando en la pocision 0 de las listas sea igual a municipio, agarre las 16 listas debajo de ella y sume la pocision 4 de todas ellas
            cont2=0
            for lista in listaA:
                cont2=cont2+1
                for elemento in lista:
                    if lista[0] == municipio2:
                        pos2=cont2-1


            num_mujeres=0
            for lista in listaA[pos2+1:pos2+17]:
                num_mujeres=int(num_mujeres)+int(lista[4])


            porcentaje=(num_nacimientos_15_19 / num_mujeres)*100

        else:
            print("Municipio no disponible")

    return porcentaje


#Ejercicio 4


def mayorAñosMadresAdolecentes (año):
    if not año.isdigit():
    # revisamos si el año que dio si es numero, si no lo es regresamos error
        print("Error, ingresa un año")
    if int(año)<2010 or int(año)>2017:
        print("Solo tenemos disponibles desde el 2010 hasta el 2017")
    archivo= open('Nacimientos_registrados_2010_2017.csv')
#abrimos archivos y revisamos si el numero que dio el usuario si es entre el 2010 y 2017
    archivo.readline()
# leemos el archivo con linea
    i=2+6*(int(año)-2010)
#Creamos una i, la cual va a ser la posicion que utulizaremos
    #La i primero pense en elimienar el año que nos dan por el menor año posible que el usuarios nos puede dar
    #De ahi nso da el numero de año que quiere, despues de eso el numero lo multiplicas por 6 que son las
    #posiciones entre años y 2 que son las poisiciones entre los datos que necesitamos.
    linea=archivo.readline().split(",")
    niñosMaximo=int(linea[i])
    municipioMaximo=linea[0]
    #Creamos un maximo que el la primera posicion de la lista
    lineaMayor = linea
    #La linea mayor es para el punto extra
    while linea!=[""]:
        linea=archivo.readline().split(",")
        #Cuando se termine de leer el archivo y solo lea lo del blanco te da el [""]
        #esto lo vimos en el ejercicio 2.
        #Creamos esta exepcion para el error
        if linea==[""]:
            break
        #si ya se acabo entonces rompemos de donde estamos
        niños=int(linea[i])
        municipio=linea[0]
        #Igualamos las variables al maximo que tenemos ya con lo que analizamos del todo el archivo
        if niños>niñosMaximo:
            niñosMaximo=niños
            municipioMaximo=municipio
#De aqui ya empieza los puntos extras


#Ejercicio 5

def menorAñosMadresAdolecentes (año):
    if not año.isdigit():
    # revisamos si el año que dio si es numero, si no lo es regresamos error
        print("Error, ingresa un año")
    if int(año)<2010 or int(año)>2017:
        print("Solo tenemos disponibles desde el 2010 hasta el 2017")
    archivo= open('Nacimientos_registrados_2010_2017.csv')
#abrimos archivos y revisamos si el numero que dio el usuario si es entre el 2010 y 2017
    archivo.readline()
# leemos el archivo con linea
    i=2+6*(int(año)-2010)
#Creamos una i, la cual va a ser la posicion que utulizaremos
    #La i primero pense en elimienar el año que nos dan por el menor año posible que el usuarios nos puede dar
    #De ahi nso da el numero de año que quiere, despues de eso el numero lo multiplicas por 6 que son las
    #posiciones entre años y 2 que son las poisiciones entre los datos que necesitamos.
    linea=archivo.readline().split(",")
    niñosMinimo=int(linea[i])
    municipioMinimo=linea[0]
    #Creamos un maximo que el la primera posicion de la lista

    while linea!=[""]:
        linea=archivo.readline().split(",")
        #Cuando se termine de leer el archivo y solo lea lo del blanco te da el [""]
        #esto lo vimos en el ejercicio 2.
        #Creamos esta exepcion para el error
        if linea==[""]:
            break
        #si ya se acabo entonces rompemos de donde estamos
        niños=int(linea[i])
        municipio=linea[0]
        #Igualamos las variables al maximo que tenemos ya con lo que analizamos del todo el archivo
        if niños<niñosMinimo:
            niñosMinimo=niños
            municipioMinimo=municipio
    return municipio

def menu():
    print("************************************Menu**************************************")
    print("ENTER AN OPTION BETWEEN 1 TO 6 DEPENDING THE DATA YOU WANNA FIND")
    opcion = input("""
                      1: Percentage of the years of teen moms in the state and year you choose
                      2: The year with less teen moms
                      3: Percentage of teens with less than 15 yeras that were mothers in 2015
                      4: State with more teen moms
                      5: State with less teen moms
                      6: Exit
                      Enter the option:""")
    return opcion

opcion=""
while opcion != "6":
    opcion=menu()
    if opcion == "1":
        municipio=input("Enter the state you want to find: ")
        año=input("Enter the year: ")

        respuesta=percentaje_birth(municipio,año)
        print(f"Percentage of the birth of teens in: ")
        print(f"{municipio}, {año}: {respuesta}%")

    elif opcion == "2":
        municipio=input("Enter the state: ")
        print(menorAñosMadresAdolecentes(municipio))

    elif opcion == "3":
        municipio=input("Enter the state: ")

        respuesta=madres_menores_2015(municipio)
        print("Percentage of teens less than 15 that gave birth:  ")
        print(f"{municipio}, 2015: {respuesta}%")


    elif opcion== "4":
        año=input("Enter the year: ")
        print(mayorAñosMadresAdolecentes(año))

    elif opcion=="5" :
        año=input("Enter the year: ")
        print(menorAñosMadresAdolecentes(año))

    elif opcion == "6":
        print("Thanks for seen my code")
