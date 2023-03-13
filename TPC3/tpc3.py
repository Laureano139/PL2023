
import re
import json

# -------------------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------- /////////////////////////////////// ---------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------------------- #


def parse():
    with open("processos.txt", 'r') as file:
        linhas = file.readlines()

    lista = []
    for linha in linhas:
        campos = linha.strip().split("::")
        if campos[0].isdigit():
            dic = {
                'pasta': int(campos[0]),
                'data': campos[1],
                'nome': campos[2],
                'pai': campos[3] if campos[3] != "" else "::",
                'mae': campos[4] if campos[4] != "" else "::",
                'observacoes': campos[5] if len(campos) > 5 else ""
            }
            lista.append(dic)
    return lista


# -------------------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------- /////////////////////////////////// ---------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------------------- #


def processos_por_ano(lista):
    
    print("|--------------------------------|")
    print("|-----------ALINEA (A)-----------|")
    print("|--------------------------------|")
    
    
    lista = parse()

    contagem = {}


    for processo in lista:
       
        ano = int(processo['data'].split('-')[0])
        if ano in contagem:
            contagem[ano] += 1
        else:
            contagem[ano] = 1

    return contagem


# -------------------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------- /////////////////////////////////// ---------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------------------- #


def nomes_por_seculo(lista):
    
    print("|--------------------------------|")
    print("|-----------ALINEA (B)-----------|")
    print("|--------------------------------|")
    
    nomes_seculo = {}
    apelidos_seculo = {}

    regex_primeiro_nome = re.compile(r'^\w+')
    regex_ultimo_nome = re.compile(r'\w+$')

    for processo in lista:
        ano = int(processo["data"].split('-')[0])
        seculo = (ano - 1) // 100 + 1
        
        #* Com Regex
        # 
        # data = re.search(":(\d{4})-", linha)
        #    if data is not None:
        #        ano = int(data.group(1))
        #        seculo = (ano - 1) // 100 + 1
        # 
        #*#
        
        nome_completo = processo['nome']
        primeiro_nome = regex_primeiro_nome.search(nome_completo).group()
        ultimo_nome = regex_ultimo_nome.search(nome_completo).group()

        if seculo not in nomes_seculo:
            nomes_seculo[seculo] = {}
        if primeiro_nome not in nomes_seculo[seculo]:
            nomes_seculo[seculo][primeiro_nome] = 1
        else:
            nomes_seculo[seculo][primeiro_nome] += 1

        if seculo not in apelidos_seculo:
            apelidos_seculo[seculo] = {}
        if ultimo_nome not in apelidos_seculo[seculo]:
            apelidos_seculo[seculo][ultimo_nome] = 1
        else:
            apelidos_seculo[seculo][ultimo_nome] += 1

    top5 = []
    for seculo in nomes_seculo:
        nomes_comuns = sorted(nomes_seculo[seculo].items(), key=lambda x: x[1], reverse=True)[:5]
        apelidos_comuns = sorted(apelidos_seculo[seculo].items(), key=lambda x: x[1], reverse=True)[:5]
        top5.append((seculo, nomes_comuns, apelidos_comuns))
        
    for seculo in top5:
        print("Século:", seculo[0])
        print("------//------")
        print("Nomes:")
        for nome in seculo[1]:
            print(f"{nome[0]}: {nome[1]}")
        print("------//------")
        print("Apelidos:")
        for apelido in seculo[2]:
            print(f"{apelido[0]}: {apelido[1]}")
        print("")
        print("|--------//--------|")
        print("|Mudança de Século!|")
        print("|--------//--------|\n")

    return top5


# -------------------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------- /////////////////////////////////// ---------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------------------- #


def freq_relacoes(lista):
    
    print("|--------------------------------|")
    print("|-----------ALINEA (C)-----------|")
    print("|--------------------------------|")
    
    relacoes = {}
    for processo in lista:
        observacao = processo['observacoes']
        match = re.search(r'([a-z\s]+),\s*(\w+\s+\w+)\.', observacao, re.IGNORECASE)
        if match:
            parentesco = match.group(1).strip().lower()
            relacao = match.group(2).strip().lower()
            if parentesco not in relacoes:
                relacoes[parentesco] = {}
            if relacao not in relacoes[parentesco]:
                relacoes[parentesco][relacao] = 1
            else:
                relacoes[parentesco][relacao] += 1
    for parentesco in relacoes:
        print(f"{parentesco.title()}:")
        for relacao in relacoes[parentesco]:
            print(f"{relacao.title()}: {relacoes[parentesco][relacao]}")
        print()
    # return relacoes


# -------------------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------- /////////////////////////////////// ---------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------------------- #


def registos_json():
    
    with open('processos.txt', 'r', encoding='utf8') as f:

        linhas = f.readlines()[:20]

    registos_json = []

    for linha in linhas:
        campos = linha.strip().split("::")
        if campos[0].isdigit():
            registo = {
                'pasta': int(campos[0]),
                'data': campos[1],
                'nome': campos[2],
                'pai': campos[3] if campos[3] != "" else "::",
                'mae': campos[4] if campos[4] != "" else "::",
                'observacoes': campos[5] if len(campos) > 5 else ""
            }
            registos_json.append(json.dumps(registo))

    with open('registos.json', 'w') as f:
        f.write("\n".join(registos_json))
    

# -------------------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------- /////////////////////////////////// ---------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------------------- #


parsed_data = parse()
#print(parsed_data)

processos_anos = processos_por_ano(parsed_data)
print (processos_anos)

top_cinco = nomes_por_seculo(parsed_data)
#print(top_cinco)

rel = freq_relacoes(parsed_data)
#print(rel)

registos_json()