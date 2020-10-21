import random, string, io

morse = [
    ".- ", "-... ", "-.-. ", "-.. ", ". ",
    "..-. ", "--. ", ".... ", ".. ", ".--- ",
    "-.- ", ".-.. ", "-- ", "-. ", "--- ",
    ".--. ", "--.- ", ".-. ", "... ", "- ",
    "..- ", "...- ", ".-- ", "-..- ", "-.-- ", "--.. ", "   " ]

alfabeto = [ 
    "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z", " "]

def transformar(palabra):
    OW = list(palabra) # Old Word
    NW = [""]       #New Word
    r1 = len(OW)
    r2 = len(alfabeto)
    
    for i in range(r1):
        for j in range(r2):
            if OW[i] == alfabeto[j]:
                NW.append(morse[j])
        
    
    palabraARetornar = ""

    for element in NW:
        palabraARetornar += element

    palabraAReturn retornar

def manual():
    print("\nIngrese su oración y se retornará en código morse")
    print("\n")
    oracion = input()
    oracion.lower()
    nuevaOracion = transformar(oracion)
    print("\n {x}".format( x= nuevaOracion ))

def automatico():
    archivo = open("Morse Translator/exampleWords.txt", "r")
    contenido = list(archivo)
    linea = random.randrange(0, len(contenido))

    palabra = contenido[linea]

    print("\n  {x}".format( x = palabra))
    print("\n {y}".format( y = transformar(palabra)))

def main():
    print("Desea hacerlo automático o ingresar una palabra? A/M")
    x = input()
    x.lower()
    if (x == 'a'): automatico()
    else: manual()

main()