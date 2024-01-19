import requests
import json

cep = int(input('Digite o CEP solicitado: '))

api_cep = f'https://viacep.com.br/ws/{cep}/json/'
response = requests.get(api_cep)

if response.status_code == 200:
    data = response.json()
    if 'cep' in data:
        resultado_tupla = (
            ('CEP', data['cep']),
            ('Logradouro', data['logradouro']),
            ('Complemento', data['complemento']),
            ('Bairro', data['bairro']),
            ('Localidade', data['localidade']),
            ('Uf', data['uf']),
            ('IBGE', data['ibge']),
            ('GIA', data['gia']),
            ('DDD', data['ddd']),
            ('Siafi', data['siafi'])
        )
        resultado_string = ""

        for item in resultado_tupla:
            resultado_string += f'{item[0]}: {item[1]}\n'

        webhook_url = "https://discord.com/api/webhooks/1196925705364193320/{Token}"
        headers = {"Content-Type": "application/json"}
        payload = {"content": resultado_string}
        response_discord = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

        if response_discord.status_code == 204:
            print('Mensagem enviada para o Discord com sucesso!')
        else:
            print('Erro ao enviar mensagem para o Discord. Status de resposta:', response_discord.status_code)
    else:
        print('CEP não encontrado.')
else:
    print('Erro no request. O status de resposta foi:', response.status_code)