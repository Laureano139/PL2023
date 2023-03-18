
import ply.lex as lex 
import re 


print("\n")
print("//-----------  TPC 5  -----------//")
print("//------                   ------//")
print("//----  CABINE TELEFÓNICA  ----//\n")
print(">>> Afonso Amorim")
print(">>> a97569")
print("\n")

tokens = (
    "LEVANTAR",
    "POUSAR",
    "MOEDA",
    "CONTACTO",
    "ABORTAR"
)

sLEVANTAR = r"LEVANTAR"
sPOUSAR = r"POUSAR"
sABORTAR = r"ABORTAR"

money = 0
estado = 0 # 0 se telefone pousado || 1 se telefone levantado || 2 se for para abortar

def sMOEDA(s):
    reg = re.compile(r"MOEDA\s((\w+\,?\s?)+)")
    match = re.match(reg, s.value)
    s.value = match.group(1)
    return s

def sCONTACTO(s):
    rdigits = re.compile(r"T\=(\d{9})")
    match = re.match(rdigits, s.value)
    s.value = match.group(1)
    return s

def sError(s):
    print("Erro")
    s.lexer.skip(1)
    
def sWS(s):
    r"\s+"
    pass

def sSaldo(): 
    global money
    euros = int(money/100)
    cents = round(money/100 - int(money/100), 2)
    saldo_completo = str(euros) + "€" + str(int(cents*100)) + "cents."
    return saldo_completo

def moedasIntroduzidas (coinsList):
    global money 
    resE = re.findall("\d+(?=e)", coinsList)
    resC = re.findall("\d+(?=c)", coinsList)
    mResponse = "[MACHINE] -> "
    moedasCents = re.findall(r"^(1|2|5|10|20|50)$")
    moedasEuros = re.findall(r"^(1|2)$")
    
    for num in resC:
        if int(num) not in moedasCents:
            mResponse += str(num) + "moeda é inválida (cents)"
        else:
            money += int(num)
            
    for num in resE:
        if int(num) not in moedasEuros:
            mResponse += str(num) + "moeda é inválida (euros)"
        else:
            money += int(num)*100
            
    mResponse += "Saldo => " + sSaldo
    print(mResponse)
    
def parseContacto(contacto):
    global money

    if (contacto[:3] == "601" or contacto[:3] == "641"):
        print("[MACHINE] -> Não é possível contactar números começados por [601] ou [641]!")
    
    elif (contacto[:2] == "00"):
        if (money > 150):
            money -= 150
            print("[MACHINE] -> saldo = " + sSaldo())
        else:
            print("[MACHINE] -> Saldo Insuficiente")

    elif (contacto[:1] == "2"):
        if (money > 25):
            mmoney -= 25
            print("[MACHINE] -> saldo = " + sSaldo())
        else:
            print("[MACHINE] -> Saldo Insuficiente")

    elif (contacto[:3] == "800"):
        print("[MACHINE] -> saldo = " + sSaldo())

    elif (contacto[:3]):
        if (money > 10):
            money -= 10
            print("[MACHINE] -> saldo = " + sSaldo())
        else:
            print("[MACHINE] -> Saldo Insuficiente")
    else: print("[MACHINE] -> Contacto inválido")

def parse(token):
    global flag 

    if (token.type == "LEVANTAR"):
        if (flag == 0): 
            print("[MACHINE] ->  Introduza moedas para efetuar uma chamada: ")
            flag = 1
        else: print("[MACHINE] ->  O telefone já se encontra levantado!")
    
    elif (token.type == "POUSAR"):
        if (flag == 1): 
            saldoFinal = sSaldo()
            print("[MACHINE] ->  Troco =" + saldoFinal)
            flag = 0
        else: print("[MACHINE] ->  O telefone já se encontra pousado!")

    elif (token.type == "MOEDA"):
        if(flag == 0):
            print("[MACHINE] ->  O telefone está pousado")
        else: moedasIntroduzidas(token.value)

    elif (token.type == "CONTACTO"):
        if (flag == 0):
            print("[MACHINE] ->  O telefone está pousado")
        else: parseContacto(token.value)
    
    elif (token.type == "ABORTAR"):
        flag = 2
    else:
        print("Input error! Try again!")



def lexerr():
    lexer = lex.lex()
    while(True):
        info = input(">>> ")
        lexer.input(info)
        for token in lexer:
            parse(token)
        if (flag == 2): break

lexerr()