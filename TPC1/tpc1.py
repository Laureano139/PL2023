from typing import List, Tuple, Union
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

def disease_dist(pacientes: list) -> str:
    dist = {'M': 0, 'F': 0}
    for paciente in pacientes:
        sexo = paciente["sexo"]
        doenca = paciente["temDoenca"]
        if doenca:
            dist[sexo] += 1
    return f'M: {dist["M"]}, F: {dist["F"]}'

#--------------------------------------------------------------------------------------------------------------------------------------#

def faixa_etaria_dist(pacientes):
    dist = {}
    
    for i in range(0, max(int(paciente["idade"]) for paciente in pacientes) + 5, 5):
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
    
    print("Distribuicao da doenca por faixa etaria:\n")
    for faixa_etaria, contadores in dist.items():
        total = contadores["Com_doenca"] + contadores["Sem_doenca"]
        if total > 0:
            percent_doente = contadores["Com_doenca"] / total * 100
        else:
            return 0
        print(f"{faixa_etaria}: {percent_doente:.1f}% <---> {contadores['Com_doenca']} de {total} doentes.")

#def colestrol_dist(pacientes):

# parsed_data = parse()
# print(parsed_data)

# disease_data = disease_dist(parsed_data)
# print(disease_data)

#faixa_etaria_dist(parse_csv())

    
        
    

    