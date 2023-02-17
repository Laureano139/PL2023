
import re 

file = open("myheart.csv","r")

info = file.read()

lines = info.splitlines()[1:] # -> Slice a partir da primeira linha

def parse(lines):
    pacientes = []
    for line in lines:
        idade,sexo,tensao,colesterol,batimento,temDoenca = line.strip().split(",") # -> Remover os espaços e separar a linha por vírgulas
        pacientes.append({
            line["idade"]: int(idade),
            line["sexo"]: sexo,
            line["tensao"]: int(tensao),
            line["colestrol"]: int(colesterol),
            line["batimento"]: int(batimento),
            line["temDoenca"]: bool(int(temDoenca))
        })
    return pacientes

def disease_dist(pacientes):
    dist = {}
    
    dist["M"] = 0
    dist["F"] = 0
    
    for entry in pacientes:
        if entry["temDoenca"] == 1:
            dist[entry["sexo"]] += 1
    return dist

def faixa_etaria_dist(pacientes):
    dist = {}
    
    for i in range(0, max(paciente["idade"] for paciente in pacientes) + 5, 5):
        dist[f"{i}-{i+4}"] = {"Com_doenca": 0, "Sem_doenca": 0}

    for paciente in pacientes:
        idade = paciente["idade"]
        tem_doenca = paciente["temDoenca"]
        for faixa_etaria, contadores in dist.items():
            lim_inf = int(faixa_etaria.split("-")[0])
            lim_sup = int(faixa_etaria.split("-")[1])
            if idade >= lim_inf and idade <= lim_sup:
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
        

        
    

    