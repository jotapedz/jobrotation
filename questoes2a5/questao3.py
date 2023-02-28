import json
#Abre o JSON e lê o seu conteúdo
with open('dados.json', 'r') as f:
    dados = json.load(f)

#Lista com os faturamentos diários
fat = [dia['faturamento'] for dia in dados['dias']]

#Menor valor de faturamento ocorrido em um dia do mês
menor_fat = min(fat)
print('Menor valor de faturamento diário:', menor_fat)

#Maior valor de faturamento ocorrido em um dia do mês
maior_fat = max(fat)
print('Maior valor de faturamento diário:', maior_fat)

#Número de dias no mês em que o valor de faturamento diário foi superior à média mensal
media_mensal = sum(fat) / len(fat)
dias_acima_da_media = len([dia for dia in fat if dia > media_mensal])
print('Número de dias com faturamento acima da média mensal:', dias_acima_da_media)
