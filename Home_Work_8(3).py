class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


num_input = []

while True:
    num = input('Введите число: ')
    if num == 'stop':
        break
    try:
        if num.isdigit():
            num_input.append(int(num))
        else:
            raise OwnError(f'{num} не является числом!')
    except OwnError as err:
        print(err)

print(num_input)
