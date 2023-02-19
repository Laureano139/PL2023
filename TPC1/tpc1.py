
import re 

def parse():
    with open("myheart.csv", "r") as file:
        linhas = file.readlines()[1:]
    lista = []
    for line in linhas:
        idade, sexo, tensao, colesterol, batimento, temDoenca = line.strip().split(',')
        dic = {
            "idade": int(idade),
            "sexo": sexo,
            "tensao": int(tensao),
            "colesterol": int(colesterol),
            "batimento": int(batimento),
            "temDoenca": temDoenca == '1'
        }
        lista.append(dic)
    return lista

#--------------------------------------------------------------------------------------------------------------------------------------#

def disease_dist(pacientes: list):
    dist = {'M': 0, 'F': 0}
    for paciente in pacientes:
        sexo = paciente["sexo"]
        doenca = paciente["temDoenca"]
        if doenca:
            dist[sexo] += 1
    #print(f'Informacao: \nM: {dist["M"]}, F: {dist["F"]}\n')
    return dist

print("\n")
    

def disease_table(pacientes: list):
    dist = disease_dist(pacientes)
    print("--- DISTRIBUICAO POR SEXO ---\n")
    print("Tabela da distribuicao por sexo:\n")
    print("+-----------+--------------------------------+")
    print("|    Sexo   | Número de pacientes com doença |")
    print("+-----------+--------------------------------+")
    print(f"| Masculino | {dist['M']:^30} |")
    print("+-----------+--------------------------------+")
    print(f"|  Feminino | {dist['F']:^30} |")
    print("+-----------+--------------------------------+")
    
print("\n\n\n")

#--------------------------------------------------------------------------------------------------------------------------------------#

def faixa_etaria_dist(pacientes):
    idade_min = min(paciente["idade"] for paciente in pacientes)
    idade_max = max(paciente["idade"] for paciente in pacientes)
    #print(f"Idade minima: {idade_min} anos\nIdade maxima: {idade_max} anos\n")
    
    dist = {}
    for i in range(0, idade_max + 1, 5):
        dist[f"{i}-{i+4}"] = {"Com_doenca": 0, "Sem_doenca": 0}
    
    for paciente in pacientes:
        idade = paciente["idade"]
        tem_doenca = paciente["temDoenca"]
        for faixa_etaria, contadores in dist.items():
            lim_inf = int(faixa_etaria.split("-")[0])
            lim_sup = int(faixa_etaria.split("-")[1])
            if int(idade) >= lim_inf and int(idade) <= lim_sup:
                if tem_doenca:
                    contadores["Com_doenca"] += 1
                else:
                    contadores["Sem_doenca"] += 1
                break 
    
    #print("Distribuicao da doenca por faixa etaria:\n")
    for faixa_etaria, contadores in dist.items():
        total = contadores["Com_doenca"] + contadores["Sem_doenca"]
        percent_doente = 0
        if total > 0:
            percent_doente = contadores["Com_doenca"] / total * 100
        else:
            pass
        #print(f"{faixa_etaria} anos: {percent_doente:.1f}% <---> {contadores['Com_doenca']} de {total} doentes.")
        return dist
    
print("\n")
 
def faixa_etaria_table(pacientes):
    dist = faixa_etaria_dist(pacientes)
    print("--- DISTRIBUICAO POR FAIXA ETARIA ---\n")
    print("Tabela da distribuicao por faixa etaria:\n")
    print("+------------+------------------------+-------------------------+")
    print("| Faixa etaria | Doenças                | Sem doenças           |")
    print("+------------+------------------------+-------------------------+")
    for faixa_etaria, contadores in dist.items():
        print(f"| {faixa_etaria:^11} | {contadores['Com_doenca']:^22} | {contadores['Sem_doenca']:^22} |")
        print("+------------+------------------------+-------------------------+")
    print()

print("\n\n\n")

#--------------------------------------------------------------------------------------------------------------------------------------#

def colesterol_dist(pacientes):
    colesterol_min = min(paciente["colesterol"] for paciente in pacientes)
    colesterol_max = max(paciente["colesterol"] for paciente in pacientes)
    colesterol_max_intervalo = colesterol_max + (10 - (colesterol_max % 10))
    if colesterol_max_intervalo > 610:
        colesterol_max_intervalo = 610
    #print(f'Colesterol minimo: {colesterol_min}\nColesterol maximo: {colesterol_max}\n')

    distr = {}
    for i in range(colesterol_min, colesterol_max_intervalo + 10, 10):
        distr[f"{i}-{i+9}"] = {"Doentes": 0, "Saudaveis": 0}

    for paciente in pacientes:
        colesterol = paciente["colesterol"]
        temDoenca = paciente["temDoenca"]
        for colesterol_niveis, counters in distr.items():
            limite_inf = int(colesterol_niveis.split("-")[0])
            limite_sup = int(colesterol_niveis.split("-")[1])
            if int(colesterol) >= limite_inf and int(colesterol) <= limite_sup:
                if temDoenca:
                    counters["Doentes"] += 1
                else:
                    counters["Saudaveis"] += 1
                break

    #print("Distribuicao da doenca por niveis de colesterol:\n")
    for colesterol_niveis, counters in distr.items():
        ttl = counters["Doentes"] + counters["Saudaveis"]
        if ttl > 0:
            percent = counters["Doentes"] / ttl * 100
            #print(f'Niveis de colesterol: {colesterol_niveis} -> {percent:.1f}%')
        else:
            pass
    return distr

print("\n")

def colesterol_table(pacientes):
    distr = colesterol_dist(pacientes)
    print("--- DISTRIBUICAO POR COLESTEROL ---\n")
    print("Tabela da distribuição da doença por níveis de colesterol:\n")
    print("+----------------------+------------------------+------------------------+")
    print("| Níveis de colesterol |        Doenças         |       Sem doenças      |")
    print("+----------------------+------------------------+------------------------+")
    for colesterol_niveis, contadores in distr.items():
        print(f"| {colesterol_niveis:^20} | {contadores['Doentes']:^22} | {contadores['Saudaveis']:^22} |")
        print("+----------------------+------------------------+------------------------+")
    print()

print("\n\n\n")

#--------------------------------------------------------------------------------------------------------------------------------------#

parsed_data = parse()

disease_data = disease_dist(parsed_data)

faixa_etaria_data = faixa_etaria_dist(parsed_data)

colesterol_data = colesterol_dist(parsed_data)

table1_data = disease_table(parsed_data)

table2_data = faixa_etaria_table(parsed_data)

table3_data = colesterol_table(parsed_data)