import pandas as pd
from pycoingecko import CoinGeckoAPI
from coin_gecko import *
cg = CoinGeckoAPI()


# TODO!
def predict_prices(currency):
    placeholder_prices = {
        'bitcoin': {'01-08-2045': 1.1},
        'ethereum': {'01-08-2045': 2.1},
        'ripple': {'01-08-2045': 3.1}
    }
    return placeholder_prices[currency]


#prices = cg.get_price(ids='bitcoin,ethereum,ripple', vs_currencies='usd')
#print(prices)

prices2 = get_single_price('bitcoin', "1-6-2013")
print(prices2)
