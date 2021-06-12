# código fonte em Python versão 3.9.5 

import csv  # importando a biblioteca csv para trabalhar este formato no python.
from math import radians, sin, cos, sqrt, asin

TabelaTaxis = []  # declarando a Array vazia 'TabelaTaxis' que constará as informações de cada ponto de taxi

with open("pythonfiles/pontos_taxi.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=";", quoting=csv.QUOTE_ALL)

    # transformando linhas do .csv em 'Array múltiplo'.
    for row in reader:
        TabelaTaxis.append(row)
        
print(len(TabelaTaxis))


#Colocando o MenuPrincipal como uma function.
def MenuApp():
    print("""\n======= ESCOLHA UMA OPÇÃO =====
1. Listar todos os pontos de Táxi
2. Informar a minha localização
3. Consultar rota
4. Terminar o programa\n""")
    
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
            if escolha not in (1, 2, 3, 4):
                raise ValueError('Valor fora do limite permitido\n')
        except ValueError as e:
            print('Valor inválido: Utilizar somente números de 1 a 4.\n')
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
                    latitude1 = float(latitudeStr)
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
                    longitude1 = float(longitudeStr)
                    longitudeInt = int(longitude1)
                if longitudeInt not in range(-52,-48):
                    raise ValueError('Valor de latitude não condiz com região metropolitana de Porto Alegre\n')
            except ValueError as e:
                print(e)
            else:
                break
            
    # configurando escolha de MENU #3 onde se define as 3 paradas de táxi mais próximos do usuário.
    if escolha == 3:

        primeiroPonto = 0
        segundoPonto = 0
        terceiroPonto = 0
        
        
        
        for i in range(1, len(TabelaTaxis) - 1):
            
            
            
    if escolha == 4:  # término do loop
        break

print('Fim do programa!')