#Faturamento mensal por estado
fat = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

#Calcula o faturamento total da distribuidora
faturamento_total = sum(fat.values())

#Calcula o percentual de cada estado no faturamento total
percent = {estado: faturamento / faturamento_total * 100 for estado, faturamento in fat.items()}

#Imprime os percentuais de cada estado
for estado, percentual in percent.items():
    print(f'{estado}: {percentual:.2f}%')
