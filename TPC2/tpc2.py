
paradoNoBailao = False
soma = 0
x = ''

usr_input = input("Insira o input -> ")

while usr_input != "":
    
    if ("on" == usr_input.lower()):
        paradoNoBailao = False
    elif ("off" == usr_input.lower()):
        paradoNoBailao = True
    elif ('=' in usr_input):
        print(soma)
    elif paradoNoBailao == False:
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
                
            i += 1
                
    usr_input = input("Insira o input -> ")







                

