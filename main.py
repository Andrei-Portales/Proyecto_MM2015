import crypto
import files_read


opciones = """
Ejila el numero de opcion que desee:

1. Encriptar texto plano
2. Desencriptar texto plano
3. Encriptar archivo txt
4. Desencriptar archivo txt
5. Claves
6. Salir
"""

clavesM = """
Ejila el numero de opcion que desee:

1. Mostrar llaves actuales
2. Cambiar las llaves
3. Volver al menu principal
"""


def cleanScreen():
    for _ in range(50):
        print()


def generateNewKeys():
    salida = True
    while salida:
        cleanScreen()
        try:
            cleanScreen()
            p = int(input("Ingrese un numero primo para 'p' = "))
            q = int(input("Ingrese un numero primo para 'q' = "))
            if crypto.isPrime(p) and crypto.isPrime(q):
                res = crypto.generatePublicKeys(p, q)
                cleanScreen()
                print("Se calculo nuevos valores para las llaves \
                         \n\nn =", res["n"], "\nk =", res["k"], "\nj =", res["j"])
                input("\n\nPresione enter para continuar...")
                salida = False
            else:
                input(
                    "\n\nHas ingresado uno o mas valores los cuales no son primos \n\nPresiona enter para volver...")
        except:
            input(
                "Has ingresado un valor no numerico \n\nPresiona enter para volver a intentar...")


def showKeys():
    keys = files_read.readPublicKey()
    cleanScreen()
    print("LLaves publicas:")
    print("-", keys["n"], "\n-", keys["k"])
    print("\n\nLLave privada:")
    print("-", keys["j"])
    input("\n\nPresione enter para continuar...")


def clavesMenu():
    salida = True
    while salida:
        cleanScreen()

        print(clavesM)
        opcion = input("opcion: ")
        if opcion == "1":
            showKeys()
        elif opcion == "2":
            generateNewKeys()
        elif opcion == "3":
            salida = False


def encriptacionTextoPlano():
    cleanScreen()
    texto = input("Ingrese el texto a encriptar = ")
    encriptado = crypto.encriptar(texto)
    texto = ""
    for n in encriptado:
        texto = texto + str(n) + " "
    print("\nTexto encriptado =", texto)
    input("\n\nPresione enter para volver al menu...")


def desencriptarTextoPlano():
    cleanScreen()
    texto = input("Ingrese el texto a desencriptar = ")
    texto = texto.split(" ")
    txtDesencriptado = []
    for n in texto:
        try:
            num = int(n)
            txtDesencriptado.append(num)
        except:
            print()
    try:
        result = crypto.desencriptar(txtDesencriptado)
        print("\n\nTexto desencriptado =", result)
        input("\n\nPresione enter para volver al menu...")
    except:
        cleanScreen()
        print("Ocurrio un error al desencriptar el mensaje")
        input("\n\nPresione enter para volver al menu...")


def encriptacionTxt():
    cleanScreen()

    try:
        name = input("Ingrese el nombre del archivo a encriptar = ")
        lines = files_read.readTxt(name)
        result = []
        for line in lines:
            res = crypto.encriptar(line)
            prov = ""
            for byte in res:
                prov = prov + str(byte) + " "
            result.append(prov)
        file_name = "archivo_encriptado.txt"
        files_read.writeTxt(file_name, result)

        print("\n\nTexto encriptado se guardo en:", file_name)
        input("\n\nPresione enter para volver al menu...")

    except:
        cleanScreen()
        print("Ocurrio un error al encriptar el archivo")
        input("\n\nPresione enter para volver al menu...")

def desencriptacionTxt():
    cleanScreen()

    try:
        name = input("Ingrese el nombre del archivo a desencriptar = ")
        lines = files_read.readTxt(name)
        result = []
        for line in lines:
            split = line.split(" ")
            byteList = []
            for n in split:
                try:
                    byteList.append(int(n))
                except:
                    print()
            result.append(crypto.desencriptar(byteList))
        file_name = "archivo_desencriptado.txt"
        files_read.writeTxt(file_name, result)

        print("\n\nTexto desencriptado se guardo en:", file_name)
        input("\n\nPresione enter para volver al menu...")

    except:
        cleanScreen()
        print("Ocurrio un error al desencriptar el archivo")
        input("\n\nPresione enter para volver al menu...")



def menu():
    salida = True
    while salida:
        cleanScreen()
        print(opciones)
        opcion = input("opcion: ")

        if opcion == "1":
            encriptacionTextoPlano()
        elif opcion == "2":
            desencriptarTextoPlano()
        elif opcion == "3":
            encriptacionTxt()
        elif opcion == "4":
            desencriptacionTxt()
        elif opcion == "5":
            clavesMenu()
        elif opcion == "6":
            cleanScreen()
            print(" --- Fin del programa ---\n\n")
            exit(0)


menu()
