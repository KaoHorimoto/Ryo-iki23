sum = 0

for i in range(0, 1000):
    file_name = f'kitamura_{i:05d}_kgu.txt'
    path = f'sample/{file_name}'
    with open(path, 'r') as file:
        number = int(file.read())
        if number % 2 != 0:
            sum += number

print("合計:", sum)