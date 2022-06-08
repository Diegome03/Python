

import requests
import time

cripto = input("Introduce la criptomoneda a seguir: ")
while True:
    r = requests.get(f'https://api.coinbase.com/v2/exchange-rates?currency={cripto}') 
    print("---------------------------------------------------")
    print(r.json()['data']['rates']['EUR']) 
    print("---------------------------------------------------")
    time.sleep(5)

