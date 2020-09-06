class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_num_1 = input("Введите делимое: ")
inp_num_2 = input("Введите делитель: ")

try:
    inp_num_1 = int(inp_num_1)
    inp_num_2 = int(inp_num_2)
    if inp_num_2 == 0:
        raise OwnError("Деление на ноль недопустимо!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Результат деления: {inp_num_1 / inp_num_2}")
