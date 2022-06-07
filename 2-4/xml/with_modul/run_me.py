import utils

Valute = input("Ввыедит аббревиатуру  валюты - ").upper()
print(utils.currency_rates(Valute))