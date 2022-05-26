numbers_user = []
print("Число должно быть целым и положительным")
num_one = input ('Введите количество секунд (первое значение) ')
num_two = input ('Введите количество секунд (второе значение) ')
numbers_user.append(num_one)
numbers_user.append(num_two)

for int_valid in numbers_user:
    if int_valid.isdigit():
        int_valid = int(int_valid)
        
    else:
        print("Введеные данные не корректные")
        print("Выход из прраммы.")
        exit()


second_statik = 1
minute_statik = 60
hour_statik = 3600
day_statik = 86400
week_statik = 604800
mounth_statik = 2629743
year_statik = 31556926 

for element in numbers_user:
    element = int(element)
    
    day_result = element // day_statik
    hour_result = (element % day_statik) // hour_statik
    minute_result = ((element % day_statik) % hour_statik) // minute_statik
    second_result = ((element % day_statik) % hour_statik) % minute_statik
    
    if day_result > 0:
        print(f"{day_result} дн {hour_result} час {minute_result} мин {second_result} сек")

    elif hour_result > 0:
        print(f"{hour_result} час {minute_result} мин {second_result} сек")
    
    elif minute_result > 0:
            print(f"{minute_result} мин {second_result} сек")
    
    elif second_result >= 0:
            print(f"{second_result} сек")
