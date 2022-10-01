
#todo: hacer un programa, usando la pogramación orientada a objetos, que me permita calcular la cantidad de ingradientes
#todo / necesarios para hacer una torta según un peso específico de la torta final, que me permita cambiar la receta de la torta
#todo / que use las propiedades fisicas y químicas de los materiales (densidad, peso, viscosidad, concentración, etc)

#todo / el nombre de la clase será "torta", las variables serán la cantidad de ingredientes, y las funciones serán los calculos 
#todo / de los ingredientes, las concentraciones, y cosas así. hasta ahora solo abrá dos objetos (dos recetas de torta), y una clase.

def valid_str(resp,cond):           # validar una str en base a otra str, que puede representar un solo elemento o varios

    print()

    if resp == cond:

        print("respuesta acepada")
        print()
    
    else:

        if cond.count(",") >= 1:    # si son varias palabras de condicion

            cond = cond.split(",")     # aquí separo las palabras de condición en una lista

            k = 0

            while k == 0:

                for i in cond:

                    if resp == i:

                        k += 1

                if k == 1:

                    print("respuesta aceptada")
                    print()
                
                else:

                    resp = input("ingresa una respuesta válida: ")
                    print()

        else:    # si es una sola palabra de condición
           
            k = 0

            while k == 0:

                resp = input("ingresa una respuesta válida: ")
                print()

                if resp == cond:

                    k += 1

            else:

                print("respuesta aceptada")
                print()



#! --------------------------------------------------------------------------



lista_recetas = []

class Torta():

    def __init__(self, codigo, nombre, descripcion, harina, azucar, leche, aceite, chocolate, vinagre, vainilla, huevos, bicarbonato, sal, mantequilla):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.harina = harina
        self.azucar = azucar
        self.leche = leche
        self.aceite = aceite
        self.chocolate = chocolate
        self.vinagre = vinagre
        self.vainilla = vainilla
        self.huevos = huevos
        self.bicarbonato = bicarbonato
        self.sal = sal
        self.mantequilla = mantequilla



    def __str__(self):
        return """codigo: {}\tnombre: {}
descripcion: {}\tharina: {}
azucar: {}\tleche: {}
aceite: {}\tchocolate: {}
vinagre: {}\tvainilla: {}
huevos: {}\tbicarbonato: {}
sal: {}\tmantequilla: {}\n\n""".format(self.codigo,self.nombre,self.descripcion,self.harina,self.azucar,self.leche,self.aceite,self.chocolate,self.vinagre,self.vainilla,self.huevos,self.bicarbonato,self.sal,self.mantequilla)



    def vari_recet(self):

        var = float(input("¿cuál es el tamaño de la torta respecto al tamaño normal?: "))

        #codigo = int(input("¿cuál es el código de la receta de la torta que quieres alterar?"))

        #for i in lista_recetas:

         #   if i.codigo == codigo:
                
        print("nombre: {} \t descripción: {} \n\nharina: {} \t azucar: {} \nleche: {} \t aceite: {} \nchocolate: {} \t vinagre: {} \nvainilla: {} \t huevos: {} \nbicarbonato: {} \t sal: {} \nmatequilla: {} ".format(self.nombre,self.descripcion,self.harina*var,self.azucar*var,self.leche*var,self.aceite*var,self.chocolate*var,self.vinagre*var,self.vainilla*var,self.huevos*var,self.bicarbonato*var,self.sal*var,self.mantequilla*var))



    def ajustar_receta(self):

        codigo = int(input("confirma el código de la receta a ajustar: "))

        #for i in lista_recetas:
    
            #if codigo == i.codigo:

        ajus_rec = i

        k = 0

        while k == 0:

            ajus = input("0 - nombre \t 1 - descripcion \t 2 - harina \n 3 - azúcar \t 4 - leche \t 5 - aceite \n 6 - chocolate \t 7 - vinagre \t 8 - vainilla \n 9 - huevos \t 10 - bicarbonato \t 11 - sal \n 12 - mantequilla \t 13 - para salir \n\n ¿qué parámetro desea ajustar?")

            valid_str(ajus,"0,1,2,3,4,5,6,7,8,9,10,11,12,13")
            
            if ajus == "13":

                print("saliendo...")
                k += 1

            elif ajus == "0" and k == 0:
                #i.nombre = input("editar nombre: ")
                ajus_rec.nombre = input("editar nombre: ")

            elif ajus == "1" and k == 0:
                #i.descripcion = input("edita la descripción: ")
                ajus_rec.descripcion = input("edita la descripción: ")

            elif ajus == "2" and k == 0:
                #i.harina = float(input("ajusta la cantidad de harina: "))
                ajus_rec.harina = int(input("ajusta la cantidad de harina: "))

            elif ajus == "3" and k == 0:
                #i.azucar = float(input("ajusta la cantidad de azucar: "))
                ajus_rec.azucar = int(input("ajusta la cantidad de azucar: "))

            elif ajus == "4" and k == 0:
                #i.leche = float(input("ajusta la cantidad de leche: "))
                ajus_rec.leche = int(input("ajusta la cantidad de leche: "))
            
            elif ajus == "5" and k == 0:
                #i.aceite = float(input("ajusta la cantidad de aceite: "))
                ajus_rec.aceite = int(input("ajusta la cantidad de aceite: "))
            
            elif ajus == "6" and k == 0:
                #i.chocolte = float(input("ajusta la cantidad de chocolate: "))
                ajus_rec.chocolte = int(input("ajusta la cantidad de chocolate: "))
            
            elif ajus == "7" and k == 0:
                #i.vinagre = float(input("ajusta la cantidad de vinagre: "))
                ajus_rec.vinagre = int(input("ajusta la cantidad de vinagre: "))
            
            elif ajus == "8" and k == 0:
                #i.vainilla = float(input("ajusta la cantidad de vainila: "))
                ajus_rec.vainilla = int(input("ajusta la cantidad de vainila: "))
            
            elif ajus == "9" and k == 0:
                #i.huevos = float(input("ajusta la cantidad de huevos: "))
                ajus_rec.huevos = int(input("ajusta la cantidad de huevos: "))
            
            elif ajus == "10" and k == 0:
                #i.bicarbonato = float(input("ajusta la cantidad de bicarbonato: "))
                ajus_rec.bicarbonato = int(input("ajusta la cantidad de bicarbonato: "))
            
            elif ajus == "11" and k == 0:
                #i.sal = float(input("ajusta la cantidad de sal: "))
                ajus_rec.sal = int(input("ajusta la cantidad de sal: "))
            
            elif ajus == "12" and k == 0:
                #i.mantequilla = float(input("ajusta la cantidad de mantequila: "))
                ajus_rec.mantequilla = int(input("ajusta la cantidad de mantequila: "))

        for i in lista_recetas:

            if codigo == i.codigo:

                del lista_recetas[lista_recetas.index(i)]
                lista_recetas.append(ajus_rec)



def act_local():
    
    arch = open("recetas_de_tortas.txt","r")

    re_in = arch.read()

    arch.close()

    if len(re_in) == 0:

        print("no hay recetas para mostrar")

    elif len(re_in) > 0:

        if "\n\n" in re_in:

            re_in = re_in.split("\n\n")

            for i in re_in:

                coso = i.split("\n")

                lista = []

                for i in coso:

                    coso = i.split("\t")
                    lista.append(coso[0])
                    lista.append(coso[1])

                lista_2 = []

                for i in lista:

                    lista_2.append(i[-1])
                    int(lista_2[-1])

                codigo,nombre,descripcion,harina,azucar,leche,aceite,chocolate,vinagre,vainilla,huevos,bicarbonato,sal,mantequilla = lista_2

                obj_torta = Torta(codigo,nombre,descripcion,harina,azucar,leche,aceite,chocolate,vinagre,vainilla,huevos,bicarbonato,sal,mantequilla)

                lista_recetas.append(obj_torta)

        elif "\n" in re_in:

            re_in = re_in.split("\n")
            
            lista = []

            for i in re_in:

                coso = i.split("\t")

                lista.append(coso[0])
                lista.append(coso[1])
                
            lista_2 = []

            for i in lista:

                lista_2.append(i[-1])
                int(lista_2[-1])

            codigo,nombre,descripcion,harina,azucar,leche,aceite,chocolate,vinagre,vainilla,huevos,bicarbonato,sal,mantequilla = lista_2

            obj_torta = Torta(codigo,nombre,descripcion,harina,azucar,leche,aceite,chocolate,vinagre,vainilla,huevos,bicarbonato,sal,mantequilla)
            print(obj_torta)
            lista_recetas.append(obj_torta)

        else:

            print("esa infoprmación está corrupta")

    x = input("local actualizado, presiona enter para continuar")


desi = input("¿cargar las recetas guardadas?: ")

valid_str(desi,"si,no")

if desi == "si":

    act_local()


def regis_torta():
    
    print("entrada de nueva receta de torta")
    print()
    codigo = int(input("código de la torta: "))
    nombre = input("nombre de la torta: ")
    descripcion = input("descripción de la torta: ")
    harina = int(input("g de harina: "))
    azucar = int(input("g de azúcar: "))
    leche = int(input("mL de leche: "))
    aceite = int(input("mL de aceite: "))
    chocolate = int(input("g de chocolate: "))
    vinagre = int(input("mL de viangre: "))
    vainilla = int(input("mL de vainilla: "))
    huevos = int(input("unidades de huevo: "))
    bicarbonato = int(input("g de bicarbonato: "))
    sal = int(input("g de sal: "))
    mantequilla = int(input("g de mantequilla: "))
    obj_torta = Torta(codigo,nombre,descripcion,harina,azucar,leche,aceite,chocolate,vinagre,vainilla,huevos,bicarbonato,sal,mantequilla)
    lista_recetas.append(obj_torta)     

    print()
    desi = input("¿desea registrar la receta en el respaldo?: ")

    valid_str(desi,"si,no")

    if desi == "si":

        cade = str(obj_torta)
        arch = open("respaldo_recetas_de_tortas.txt","a")
        arch.write(cade)
        arch.write("\n")
        arch.close()
        print()
        print("receta guardada!")

    else:

        print("ok, seguimos entonces")



def actu_regis():
    
    m = 0

    cod_1 = []

    arch = open("recetas_de_tortas.txt","r")

    re_in = arch.read()

    arch.close()

    if re_in == "":

        pass

    else:

        if "\n\n" in re_in:

            recet_1 = re_in.split("\n\n")

            for i in recet_1:

                cod_1.append(i[:i.index("\t")])

        else:

            recet_1 = re_in

            cod_1.append(recet_1[:recet_1.index("\t")])


    cod_2 = []

    arch = open("respaldo_recetas_de_tortas.txt","r")

    re_in = arch.read()

    arch.close()

    if re_in == "":

        pass

    else:

        if "\n\n" in re_in:

            recet_2 = re_in.split("\n\n")

            for i in recet_2:

                cod_2.append(i[:i.index("\t")])

        else:

            recet_2 = re_in

            cod_2.append(recet_2[:recet_2.index("\t")])



    if len(cod_2) > len(cod_1) and len(cod_2) > 1:
        
        k = 0

        for i in cod_2:
        
            if i not in cod_1:

                arch = open("recetas_de_tortas.txt","a")

                if cod_1 == [] and k == 0:

                    arch.write(recet_2[cod_2.index(i)])

                else: 

                    arch.write("\n\n")
                    arch.write(recet_2[cod_2.index(i)])

                arch.close()

                k += 1

    elif len(cod_2) == 1 and len(cod_1) == 0:

        f = 0

        arch = open("recetas_de_tortas.txt","a")

        arch.write(recet_2)

        arch.close()

        print("se guardo 1 receta")

        f += 1

    elif len(cod_1) > len(cod_2) and len(cod_1) > 1:

        k = 0
        
        for i in cod_1:
        
            if i not in cod_2:

                arch = open("respaldo_recetas_de_tortas.txt","a")

                if cod_2 == [] and k == 0:

                    arch.write(recet_1[cod_1.index(i)])

                else: 

                    arch.write("\n\n")
                    arch.write(recet_1[cod_1.index(i)])

                arch.close()

                k += 1

    elif len(cod_1) == 1 and len(cod_2) == 0:

        f = 0

        arch = open("respaldo_recetas_de_tortas.txt","a")

        arch.write(recet_1)

        arch.close()

        print("se guardo 1 receta")

        f += 1

    else:

        print("no hay nada que actualizar")

    if f == 0 and k > 0:

        print("se guardaron",k,"recetas")       
    


def guard_recet():
                               
    arch = open("recetas_de_tortas.txt","a")

    for i in lista_recetas:

        i = str(i)
        arch.write(i)
        arch.write("\n\n")

        print()
        print("receta código:",i[i.index(" "):i.index("\t")],"guardada!")

    arch.close()



def mostrar_recetas():

    desi = input("¿del local (1) o del respaldo (2)?: ")

    valid_str(desi,"1,2")

    if desi == "1":

        desi = input("¿vistazo rápido (1), o recetas completas (2)?:")
        print()

        valid_str(desi,"1,2")

        if desi == "1":

            print("estas son las recetas: ")
            print()

            for obj_torta in lista_recetas:
        
                print("código de la torta:",obj_torta.codigo,"nombre de la torta: ",obj_torta.nombre,"\tdescripción de la torta: ",obj_torta.descripcion)

        else:

            print("Estas son las recetas: ")
            print()

            for obj_torta in lista_recetas:

                print(obj_torta)

    else:

        arch = open("respaldo_recetas_de_tortas.txt","r")

        re_in = arch.read()

        arch.close()

        desi = input("¿vistazo rápido (1), o recetas completas (2)?:")
        print()
        
        valid_str(desi,"1,2")

        if desi == "1":

            print("estas son las recetas: ")
            print()

            if "\n\n" in re_in:

                re_in = re_in.split("\n\n")

                for i in re_in:

                    print(i[:i.index("\t",i.index("\n"))])

            else:

                print(re_in)

        else:

            print("estas son las recetas: ")
            print()
            
            if "\n\n" in re_in:

                re_in = re_in.split("\n")

                for i in re_in:

                    print(i)
            
            else:
                print(re_in)

        


def bus_rece():

    desi = input("buscar en el respaldo (1) o en el programa (2)?: ")

    valid_str(desi,"1,2")

    if desi == "1":

        arch = open("respaldo_recetas_de_tortas.txt","r")

        re_in = arch.read()
    
        if "\n" in re_in:

            re_in = re_in.split("\n")

            for i in re_in:

                print(i)
        
        else: 

            print(i)

    elif desi == "2":

        codigo = int(input("código de la receta a buscar: "))

        for i in lista_recetas:
    
            if codigo == i.codigo:

                print(i)



def salir():

    if len(lista_recetas) == 0:

        print("Hasta luego!")

        exit()

    else:
        
        desi = input("¿deseas guardar las recetas antes de salir?: ")

        valid_str(desi,"si,no")

        if desi == "si":

            guard_recet()
            print("recetas guardadas")
            print("hasta luego")
            exit()

        else:

            print("ok, saldremos sin guardar \n\nhasta luego!")
            exit()



def main():

    while True:

        print()

        print("|****************************|")
        print("|**|      Bienvenido      |**|")
        print("|**|         Menu         |**|")
        print("|****************************|")

        print("1 - registrar receta")
        print("2 - mostrar recetas")
        print("3 - ajustar receta")
        print("4 - variar receta")
        print("5 - buscar una receta")
        print("6 - guardar las recetas")
        print("7 - igualar local y respaldo")
        print("8 - para salir")
        print()
        deseo = input("¿qué desea hacer?: ")

        valid_str(deseo,"1,2,3,4,5,6,7,8")



        if deseo == "1":
            regis_torta()



        elif deseo == "2":

            if len(lista_recetas) == 0:
                print("no hay recetas para mostrar")
            else:
                mostrar_recetas()
    


        elif deseo == "3":

            if len(lista_recetas) == 0:
                print("no hay recetas para ajustar")
            else:
                codigo = int(input("código de la torta a ajustar: "))

                k = 1

                for i in lista_recetas:

                    print("dentro del bucle for de busqueda")

                    print("la i: ",i,"\tel codigo de la i:",i.codigo)

                    if i.codigo == codigo:

                        i.ajustar_receta()
                    
                    elif k == len(lista_recetas):
                        print("ese codigo no está, revisa lo que escribiste")

                    k += 1



        elif deseo == "4":
        
            if len(lista_recetas) == 0:
                print("no hay recetas para variar")
            else:       
                codigo = int(input("código de la receta a variar: "))

                k = 1

                for i in lista_recetas:

                    if codigo == i.codigo:

                        i.vari_recet()
        
                    elif k == len(lista_recetas):
                        print("ese codigo no está, revisa lo que escribiste")

                    k += 1



        elif deseo == "5":
            if len(lista_recetas) == 0:
                print("no hay recetas para buscar")
            else:
                bus_rece()



        elif deseo == "6":
            if len(lista_recetas) == 0:
                print("no hay recetas para guardar")
            else:
                guard_recet()



        elif deseo == "7":
            actu_regis()



        elif deseo == "8":
            salir()



if __name__ == "__main__":
    main()