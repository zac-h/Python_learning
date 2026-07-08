import sys
import requests
import json

try:
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        raise ValueError
    else:
        try:
            n = float(sys.argv[1])
        except ValueError:
            print("Command-line argument is not a number")
            raise ValueError
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=7c2fbc12fba10fe0173617fe41667811e071e58fe8952eb9934ec824fda8c01f")
    o = response.json()
#    o = {'timestamp': 1783359103234, 'data': {'id': 'bitcoin', 'rank': '1', 'symbol': 'BTC', 'name': 'Bitcoin', 'supply': '20052840.000000000000000000', 'maxSupply': '21000000.000000000000000000', 'marketCapUsd': '1280610658040.399902343750000000', 'volumeUsd24Hr': '29087152895.064350128173828125', 'priceUsd': '63861.809999999997671694', 'changePercent24Hr': '1.7755716227277205', 'vwap24Hr': '62944.00476580523', 'explorer': 'https://blockchain.info/', 'tokens': {}}}
    price = float(o["data"]["priceUsd"])
    print(f"${n*price:,.4f}")
except requests.RequestException:
    print("error")
except ValueError:
    sys.exit(1)





