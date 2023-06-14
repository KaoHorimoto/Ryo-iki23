import json

with open ('catalog.json', encoding='utf-8') as file:
    r=json.load(file)

count=0
max=0
min=1000000
for i in r:
    print(i)
    if i['name']=='jacket':
        count=count+1
        if i['price'] > max:
            max=i['price']
        if i['price'] < min:
            min=i['price']

print(count)
print(max)
print(min)

    
    







