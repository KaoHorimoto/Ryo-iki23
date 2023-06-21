sum = 0

for i in range(0, 1000):
    if i%2 != 0:
        file_name = f'kitamura_{i:05d}_kgu.txt'
        path = f'sample/{file_name}'
        with open(path, 'r') as file:
            number = int(file.read())
            sum += number
            
print("合計:", sum)