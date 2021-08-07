import requests
from currencyExchangeRates import exchangeCurrency
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

def bitcoinPrices():
    result = requests.get(url).json()

    updated = result['time']['updated']
    print(updated)

    usd_rates = result['bpi']['USD']['rate_float']
    inr = exchangeCurrency('USD','INR')
    return (usd_rates*inr)

# print(bitcoinPrices())    