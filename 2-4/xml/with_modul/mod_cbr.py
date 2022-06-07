import requests
import xmltodict
import json
import datetime

def currency_rates(type_xx):

    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
    content = json.dumps(xmltodict.parse(response.content))
    content = json.loads(content)

    date_tt =  content['ValCurs']['@Date']
    for i in content['ValCurs']['Valute']:
        if i['CharCode'] == type_xx:
            Value_float = i['Value'].replace(",", ".")
            print(f"На {date_tt} курс {i['CharCode']} составляет {float(Value_float)}")

    date_time_str = date_tt
    date_time_obj = datetime.datetime.strptime(date_time_str, '%d.%m.%Y')

    return  date_time_obj

