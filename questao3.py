import json

with  open('dados.json') as file:
    dados = json.load(file)

maximo = dados[0].get('valor')
minimo = dados[0].get('valor')
soma_valores = 0.0

# contador dos dados válidos
i = 0


for dado in dados:
    valor = dado.get('valor')
    if(valor > maximo):
        maximo = valor
    if (valor < minimo):
        minimo = valor
    if(valor != 0 ):
        i+=1
        soma_valores += valor

media = soma_valores/i

print('Maior valor: {}'.format(maximo))
print('Menor valor: {}'.format(minimo))
print('Media: {}'.format(media))



