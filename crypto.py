import files_read
import math


def modularExp(base, exponente, modulo):
    """Funcion que realiza la exponenciacion modular"""
    return pow(base, exponente, modulo)


def generatePublicKeys(p, q):
    n = p * q
    z = (p-1)*(q-1)
    c = 2
    k = 1
    salida = True
    while salida:
        mc = mcd(z, c)
        if mc == 1:
            k = int(k * c)
            salida = False
        else:
            c = c + 1

    j = generatePrivateKey(k, z)
    keys = {"n": n, "k": k, "j": j}
    files_read.writePublicKey(keys)
    keys = files_read.readPublicKey()
    return keys


def generatePrivateKey(k, z):
    j = 1
    salida = True
    while salida:
        residuo = pow((k*j), 1, z)
        if residuo == 1:
            return j
        j = j + 1


def mcd(x, y):
    mayor = max(x, y)
    menor = min(x, y)
    if ((x and y) == 0):
        menor = mayor
    else:
        r = mayor % menor
        while r != 0:
            mayor = r
            r = menor % r
            menor = mayor
    return math.fabs(menor)


def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def encriptar(texto):
    texto_cifrado = []
    llaves = files_read.readPublicKey()
    textNums = bytearray(texto, encoding= 'utf-8')

    for n in textNums:
        texto_cifrado.append(pow(n, llaves["k"], llaves["n"]))

    return texto_cifrado


def desencriptar(textoCifrado):
    texto_desifrado = bytearray()
    llaves = files_read.readPublicKey()

    for n in textoCifrado:
        texto_desifrado.append(pow(n, llaves["j"], llaves["n"]))

    return str(texto_desifrado, encoding= 'utf-8')