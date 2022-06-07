import requests
import json



def currency_rates(Valute):
    in_data = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(in_data)
    json_data = json.loads(response.content)

    for i in json_data['Valute']:
        if i == Valute:
            result = f"На {json_data['Date']} курс вылюты {json_data['Valute'][i]['CharCode']} составляет {json_data['Valute'][i]['Value']}"

    return result

if __name__ == '__main__':
    Valute = input("Ввыедит аббревиатуру  валюты - ").upper()
    print(currency_rates(Valute))