spisok_base = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

sum_elements = int(len(spisok_base))

i = 0

while i < sum_elements:
    
    #check = lambda s: not all('а' <= s <= 'я' for x in s)
    #if check(spisok_base[i]):
    if spisok_base[i].isalpha() == False:
        
        if spisok_base[i].startswith('+'):
            spisok_base[i] = spisok_base[i].zfill(3)
        else:
            spisok_base[i] = spisok_base[i].zfill(2)

        spisok_base.insert(i , '"')
        spisok_base.insert(i + 2 , '"')
        sum_elements += 2
        i += 2
    i += 1
print(spisok_base)

st = ""
for i in spisok_base:

    if i =='"' and (spisok_base[spisok_base.index(i)+1]).isalpha() != True:
        st = st +  "" + i
    elif i =='"' and (spisok_base[spisok_base.index(i)+1]).isalpha() == True: 
        st = st + i + " "
    elif i.isalpha()== True:
        st = st  + " " + i + " "
    elif i.isalpha()!=True:
         st = st  + i

print(st)
