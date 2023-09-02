import sys

def cifrar_cesar(texto, desplazamiento):
    texto_cifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            if caracter.islower():
                inicio = ord('a')
            else:
                inicio = ord('A')
            texto_cifrado += chr((ord(caracter) - inicio + desplazamiento) % 26 + inicio)
        else:
            texto_cifrado += caracter
    return texto_cifrado

if len(sys.argv) != 3:
    print("Uso: python cifrado_cesar.py <texto> <desplazamiento>")
    sys.exit(1)

texto_a_cifrar = sys.argv[1]
desplazamiento = int(sys.argv[2])

texto_cifrado = cifrar_cesar(texto_a_cifrar, desplazamiento)
print(texto_cifrado)
