prices = ['28.7','14.03','75','46.18','97.1','36.71','16.02','74.09','15.14','48.99','14.11',]
print(prices)
print(f'id списка  {id(prices)}\n')
def pricess(prices):
    str_result = ''
    i = 0
    while i < len(prices):
            temp = format(float(prices[i]), '.2f')
            prices[i] = temp
            i += 1
            rub = int(float(temp))
            kop = int(round(float(temp) % 1, 2)*100)
            kop = str(kop).zfill(2)
       
           
            str_result = str_result + f"{rub} руб {kop} коп, "
    print(str_result)

print('Вовод цен , вида -  ** руб ** коп, .. : ')
print(f'id списка  {id(prices)} \n')
pricess(prices)

print('\nВывод сортировки, от меньшего к большему: ')
print(f'id списка  {id(prices)} \n')
prices.sort(reverse=False)
pricess(prices)

print('\nВывод сортировки, от большего к меньшему: ')
print(f'id списка  {id(prices)} \n')
prices.sort(reverse=True)
pricess(prices)

print('\nСрез 5ти наибольших значений: ')
print(f'id списка  {id(prices)}\n')
pricess(prices[:5])



