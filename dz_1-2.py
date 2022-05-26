result_summ = 0
pool_numbers = []

for i in range(1, 1000, 2):
    element = i**3
    pool_numbers.append(element)

for element in pool_numbers:
    summa_local = 0
    save =element
    
    while element > 0:
        n = element % 10
        element = element // 10
        summa_local += n
        
    if (summa_local % 7) == 0:
        result_summ += save
        
print(f"{result_summ}")


print("+17 к каждому значению в списке и пересчет суммы")

result_summ = 0
pool_numbers = []

for i in range(1, 1000, 2):
    element = i**3
    pool_numbers.append(element)

pool_numbers = [i+17 for i in pool_numbers]

for element in pool_numbers:
    summa_local = 0
    save =element
    
    while element > 0:
        n = element % 10
        element = element // 10
        summa_local += n
        
    if (summa_local % 7) == 0:
        result_summ += save
        
print(f"{result_summ}")
