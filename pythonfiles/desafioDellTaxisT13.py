# código fonte em Python versão 3.9.5 

import csv  # importando a biblioteca csv para trabalhar este formato no python.
from math import radians, sin, cos, sqrt, asin

TabelaTaxis = []  # declarando a Array vazia 'TabelaTaxis' que constará as informações de cada ponto de taxi

with open("pontos_taxi.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=";", quoting=csv.QUOTE_ALL)

    # transformando linhas do .csv em 'Array múltiplo'.
    for row in reader:
        TabelaTaxis.append(row)

def virgulinha(coluna):
    for linha in range(1, len(TabelaTaxis)):
        if "," in (TabelaTaxis[linha][coluna]):
            TabelaTaxis[linha][coluna] = float(TabelaTaxis[linha][coluna].replace(",","."))


#Colocando o MenuPrincipal como uma function.
def MenuApp():
    print("""\n======= ESCOLHA UMA OPÇÃO =====
1. Listar todos os pontos de Táxi.
2. Informar a minha localização.
3. Consultar os 3 pontos de táxi mais próximos.
4. Consultar pontos de táxi por logradouro.
5. Terminar o programa\n""")
    
def haversine(lat1, lon1, lat2, lon2):
    R = 6372.8  # Earth radius in kilometers
 
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
 
    a = sin(dLat / 2)**2 + cos(lat1) * cos(lat2) * sin(dLon / 2)**2
    c = 2 * asin(sqrt(a))
 
    return R * c




# início do loop para escolha de opções
while True:
    MenuApp()

    # tratamento de erros para que a escolha seja coerente com o solicitado.
    while True:
        try:
            escolha = int(input('Digite a opção aqui: '))
            if escolha not in (1, 2, 3, 4, 5):
                raise ValueError('Valor inválido: Utilizar somente números de 1 a 5.\n')
        except ValueError as e:
            print(e)
        else:
            break

    # configurando escolha de MENU #1 para mostrar os dados de todos os pontos de táxi
    if escolha == 1:
        for pontos in TabelaTaxis:
            print(pontos)

    # configurando escolha do MENU #2, definição da localidade do usuário.
    if escolha == 2:
        
        print('Informe sua localização:')
        
        while True:
            try:
                latitudeStr = str(input('Digite sua latitude :'))
                if "-" not in latitudeStr:
                    latitudeStr = "-"+latitudeStr
                if "," in latitudeStr:
                    latitudeStr = latitudeStr.replace(",",".")
                global latitude1 
                latitude1 = -30.0011
                #latitude1 = float(latitudeStr)
                latitudeInt = int(latitude1)
                if latitudeInt not in range(-32,-28):
                    raise ValueError('Valor de latitude não condiz com região metropolitana de Porto Alegre\n')
            except ValueError as e:
                print(e)
            else:
                break

        while True:
            try:
                longitudeStr = str(input('Digite sua longitude :'))
                if "-" not in longitudeStr:
                    longitudeStr = "-"+longitudeStr
                if "," in longitudeStr:
                    longitudeStr = longitudeStr.replace(",",".")
                global longitude1
                #longitude1 = float(longitudeStr)
                longitude1 = -51.1
                longitudeInt = int(longitude1)
                if longitudeInt not in range(-52,-48):
                    raise ValueError('Valor de latitude não condiz com região metropolitana de Porto Alegre\n')
            except ValueError as e:
                print(e)
            else:
                break
            
    # configurando escolha de MENU #3 onde se define as 3 paradas de táxi mais próximos do usuário.
    if escolha == 3:
        primeiroPonto = 100.0
        segundoPonto = 100.0
        terceiroPonto = 100.0
        latitude2 = 0.0
        longitude2 = 0.0
        indiceTabelaPrimeiro = 0
        indiceTabelaSegundo = 0
        indiceTabelaTerceiro = 0
        for linha in range(1, len(TabelaTaxis)):
            latitude2 = float(TabelaTaxis[linha][6].replace(",","."))
            longitude2 = float(TabelaTaxis[linha][7].replace(",","."))
            pontoTaxi = haversine(latitude1, longitude1, latitude2, longitude2)
            if pontoTaxi < primeiroPonto:
                primeiroPonto = pontoTaxi
                indiceTabelaPrimeiro = linha
            elif primeiroPonto < pontoTaxi < segundoPonto:
                segundoPonto = pontoTaxi
                indiceTabelaSegundo = linha
            elif segundoPonto < pontoTaxi < terceiroPonto:
                terceiroPonto = pontoTaxi
                indiceTabelaTerceiro = linha
        print("As três paradas de táxi mais próximas são as seguintes: ")
        print('1- A ', str(primeiroPonto)[:4], "km.  ", end="")
        for colunas in range(2,6):
            print(str(TabelaTaxis[indiceTabelaPrimeiro][colunas]), end="-")
        print()
        print('2- A ', str(segundoPonto)[:4], " km.", end="")
        for colunas in range(2,6):
            print(str(TabelaTaxis[indiceTabelaSegundo][colunas]), end="-")
        print()
        print('3- A ', str(terceiroPonto)[:4], " km.", end="")
        for colunas in range(2,6):
            print(str(TabelaTaxis[indiceTabelaTerceiro][colunas]), end="-")
        print()
    
    if escolha == 4:
        logradouroUsuario = input("Informe o nome do logradouro que deseja fazer a busca: ").upper()
        if logradouroUsuario in TabelaTaxis

        
        
        
    if escolha == 5:  # término do loop
        break
print('Fim do programa!')