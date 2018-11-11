import requests
from prettytable import PrettyTable
listings_api = 'https://api.coinmarketcap.com/v2/listings/'
ticker_api = 'https://api.coinmarketcap.com/v2/ticker/?start='
listings_data = requests.get(listings_api).json()['data']

table = PrettyTable()
table.field_names = ['Name','Symbol','Price','Volume','MarketCap','Change 1h','Change 24h','Change 7d']

nr_coins = 0

while nr_coins < len(listings_data):

    temp_ticker_api = ticker_api + str(nr_coins)
    ticker_data = requests.get(temp_ticker_api).json()
    ticker_data = ticker_data['data']
