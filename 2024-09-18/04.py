import requests

base_url = "https://api.exchangerate-api.com/v4/latest/"

print('Qual moeda você deseja converter? ')
print('Exemplo: real = BRL, libra = GBP, peso argentino = ARS')

moeda_origem = input()

print('Você deseja converter a moeda ' + moeda_origem + ' para qual moeda? ')
print('Exemplo: real = BRL, libra = GBP, peso argentino = ARS')

moeda_alvo = input()

url = base_url + moeda_origem

resposta = requests.get(url)

cambio = resposta.json()

print(f'Cambio do {moeda_origem} da seguinte data {cambio['date']}')
print(f'1{moeda_origem} = {cambio['rates'][moeda_alvo]} {moeda_alvo}')




