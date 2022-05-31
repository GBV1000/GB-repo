num_gen = 1
while num_gen <= 100:
  if num_gen > 15:
    num_temp = num_gen%10
    if num_temp == 1:
      result = '{} процент'.format(num_gen)
      print(result)	
      num_gen +=1
    elif 2 <= num_temp < 5:
      result = '{} процента'.format(num_gen)
      print(result)	
      num_gen +=1
    else:
      result = '{} процентов'.format(num_gen)
      print(result)	
      num_gen +=1
  else:
    if num_gen == 1:
      result = '{} процент'.format(num_gen)
      print(result)	
      num_gen +=1
    elif num_gen < 5:
      result = '{} процента'.format(num_gen)
      print(result)	
      num_gen +=1    
    else:
      result = '{} процентов'.format(num_gen)
      print(result)	
      num_gen +=1
