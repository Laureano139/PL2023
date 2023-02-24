
import os

def limpar_terminal():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
limpar_terminal()

def init_page():
    print("\n")
    print("//--------  TPC 2  --------//")
    print("//---                   ---//")
    print("//---  SOMADOR ON/OFF  ----//\n")

    print(">> Afonso Amorim")
    print(">> a97569")
    print("\n")
    
    print("\nPara ajuda e contexto da aplicação, use o comando 'help'\n\n"
      "Para comandos extra use o comando 'comandos'\n")
    
init_page()

paradoNoBailao = False
soma = 0
x = ''

usr_input = input("Insira o input -> ")

while not usr_input == "":
    
    if ("help" == usr_input.lower()):
        print("\nEste mini-trabalho é baseado num somador com 3 operadores especiais ( on, off, = ).\n"
           "Para usar esta aplicação basta dar um input (numeros ou letras).\n"
           "A aplicação irá somar os numeros dados como input, sendo que, se depois colocar o operador =,\n"
           "irá devolver a soma total dos numeros dados até ao momento.\n"
           "Se usar o comando off, a aplicação irá ignorar qualquer input que for dado, tanto numeros como operadores \n"
           "sendo que o valor da soma vai ficar inalterado ao último apresentado.\n"
           "Se quiser voltar ao normal funcionamento, basta usar o comando on.\n"
           "Espero que tenha ajudado! :D \n")
    
    if ("comandos" == usr_input.lower()):
        print("\n---------- Comandos ----------\n"
              "help -> Descrição do funcionamento da aplicação;\n"
              "restart -> Limpar interface da aplicação, resetando todos os resultados previamente apresentados;\n"
              "ATENÇÃO -> COMANDO 'restart' ELIMINA TODOS OS RESULTADOS PRÉVIOS! COMEÇA TUDO DO ZERO DE NOVO!\n")
    
    if ("on" in usr_input.lower()):
        paradoNoBailao = False
    elif ("off" in usr_input.lower()):
        paradoNoBailao = True

    if paradoNoBailao == False:
    
        n = ""
        i = 0
            
        while i < len(usr_input):
            x = usr_input[i]
            
            while i < len(usr_input) and x.isdigit():
                n += x 
                i += 1
                if i < len(usr_input):
                    x = usr_input[i]
                
            if n != "":
                soma += int(n)
                n = ""
                
            if "off" in usr_input.lower():
                paradoNoBailao = True
                
            if "on" in usr_input.lower():
                paradoNoBailao = False
            
            i += 1
            
        if "=" in usr_input:
            print(soma)
           
    if ("restart" == usr_input.lower()):
        limpar_terminal()
        init_page()
        soma = 0
                    
    usr_input = input("Insira o input -> ")