
import re

def switchState(estado: bool):
    if estado == 1:
        estado = 0
    else:
        estado = 1
    return estado

def parseInput(input, estado, soma):
    
    if estado:
        sequenciasDigitos = r"\d+"
        digitos = re.findall(sequenciasDigitos, input)
        soma += [int(x) for x in digitos]
    else:
        while(ligado not in input):
            soma += 0 
    if (desligado in input.upper()):
        input = input[3:]
        switchState(estado)
    if (ligado in input.upper()):
        input = input[2:]
        switchState(estado)
    if (igual in input):
        input = input[1:]
        print("Soma atual = " + soma)
    return soma


ligado = "ON"
desligado = "OFF"
igual = '='

estado = True
soma = 0

while True:
    try:
        input = input()
        parseInput(input, estado,soma)
    except:
        break
        