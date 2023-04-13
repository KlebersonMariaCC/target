dados = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES':27165.48, 'Outros':19849.53}

valores = dados.values()

media = sum(valores)

for key,value in dados.items():
    print('{estado} : {porcentagem:.2f}'. format(estado = key, porcentagem = (value/media)*100))
