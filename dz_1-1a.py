numbers_user = []
num_one = input ('Введите первое число ')
num_two = input ('Введите первое число ')
numbers_user.append(num_one)
numbers_user.append(num_two)

sec_base = 1
min_base = 60
hour_base = 3600
day_base = 86400

number_of_elements = len(numbers_user)
num_var = 0

while (num_var + 1) <= number_of_elements:
    value_from_list = int(numbers_user[num_var])

    if value_from_list < min_base:
        print(f"{numbers_user[num_var]} сек")
        num_var += 1

    elif value_from_list < hour_base:
        mins = value_from_list // min_base
        secs = value_from_list % min_base 
        print(f"{mins} мин {secs} сек")
        num_var += 1

    elif value_from_list <= hour_base:
        h_time = value_from_list // hour_base
        mins = value_from_list % hour_base
        mins = mins // sec_base
        secs = value_from_list % sec_base 
        print(f"{h_time} час {mins}   мин {secs} сек")
        num_var += 1

    else:
        d_time = value_from_list // day_base
        h_time = (value_from_list % day_base) // hour_base
        m_time =  ((value_from_list % day_base) % hour_base) // min_base
        secs = ((value_from_list % day_base) % hour_base) % min_base 
        print(f"{d_time} дн {h_time} час {m_time} минут {secs} секунд")
        num_var += 1
    
        
