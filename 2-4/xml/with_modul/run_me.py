#from mod_cbr import currency_rates
import mod_cbr


x = input("Ведить буквенный код валюты - ").upper()
mod_cbr.currency_rates(x)
