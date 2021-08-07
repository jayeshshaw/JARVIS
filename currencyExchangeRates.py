import requests
from requests.models import Response

api_key = 'a50e67e92f22d541c1d4e73a8784a383'
url = 'https://api.currencyscoop.com/v1/latest?api_key='+api_key
def exchangeCurrency(f,t):
    results = requests.get(url).json()
    response = results['response']
    rates = response['rates']
    From = rates[f]
    To = rates[t]
    base = rates['USD']
    From = 1/From;
    ans = From*To
    return round(ans,3)

# print(exchangeCurrency('EUR','INR'))