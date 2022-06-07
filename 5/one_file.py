import requests
import json
import datetime


def currency_rates(Valute):
    in_data = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(in_data)
    json_data = json.loads(response.content)

    for i in json_data['Valute']:
        if i == Valute:
            date_type_time = datetime.datetime.strptime(json_data['Date'][0:10], "%Y-%m-%d")
            result = f"На {date_type_time} курс вылюты {json_data['Valute'][i]['CharCode']} составляет {json_data['Valute'][i]['Value']}"

    return result

Valute = input("Ввыедит аббревиатуру  валюты - ").upper()
print(currency_rates(Valute))