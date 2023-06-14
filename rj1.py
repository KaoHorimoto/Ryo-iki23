with open ('data.txt', encoding='utf-8') as file:
    total=0
    for i in file:
        try:
            print(int(i))
            total=total+int(i)
        except ValueError:
            pass
    
print(total)





