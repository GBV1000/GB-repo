import requests
import json
import pprint
import xmltodict, json
from datetime import datetime



def currency_rates(type_xx):

    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
    response.encoding = 'cp-1251"'

    content = json.dumps(xmltodict.parse(response.content))
    content = json.loads(content)

    date_tt =  content['ValCurs']['@Date']
    for i in content['ValCurs']['Valute']:
        if i['CharCode'] == type_xx:
            Value_float = i['Value'].replace(",", ".")
            date_time_obj = datetime.strptime(date_tt, '%d.%m.%Y').date()
            result = f"На {date_time_obj} курс {i['CharCode']} составляет {float(Value_float)}"

    return result

type_xx = input("Ведить буквенный код валюты - ").upper()
print(currency_rates(type_xx))