import requests

in_logs_data = requests.get("https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs")

source_data = open('source_data.txt', 'w', encoding='UTF-8')
source_data.write(in_logs_data.text)
source_data.close()

source_data = open('source_data.txt', 'r+', encoding='UTF-8')
result = []
for i in source_data:
    i =i.split(" ")
    temp = i[0], (i[5][1:]), i[6]
    result.append(temp)
print(*result, sep='\n')

source_data.close()