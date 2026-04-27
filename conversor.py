import sys
import requests

if len(sys.argv) < 2:
    sys.exit('Too few arguments')

try:
    sys_converted = float(sys.argv[1])

    response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    response.raise_for_status()

    json_text = response.json()
    bid_converted = float(json_text['USDBRL']['bid'])

except ValueError:
    sys.exit('Only float values supposed')

except requests.HTTPError:
    sys.exit('Couldn\'t complete the request')

except (requests.ConnectionError, requests.ConnectTimeout):
    sys.exit('Couldn\'t connect to the server')

cotacao = sys_converted * bid_converted

print(f'1.00 dollar is {bid_converted} reais')
print(f'* {sys_converted:.2f} dollars is {cotacao:.2f} reais')
