class Calculation:
    def __init__(self, c_num):
        self.c_num = [float(i) for i in c_num.split()]

    def __add__(self, other):
        a = self.c_num[0] + other.c_num[0]
        b = self.c_num[1] + other.c_num[1]
        sign = '+' if b >= 0 else ''
        return f'{a if a != 0 else ""}' \
               f'{sign if b != 0 else ""}' \
               f'{b if b != 0 else ""}' \
               f'{"i" if b != 0 else "0"}'

    def __mul__(self, other):
        a = self.c_num[0] * other.c_num[0] + self.c_num[0] * other.c_num[0]
        b = self.c_num[0] * other.c_num[1] + self.c_num[1] * other.c_num[0]
        sign = '+' if b >= 0 else ''
        return f'{a if a != 0 else ""}' \
               f'{sign if b != 0 else ""}' \
               f'{b if b != 0 else ""}' \
               f'{"i" if b != 0 else "0"}'


if __name__ == "__main__":
    def input_num():
        try:
            z_1 = Calculation(input('Введите веществ. и мним. часть компл. числа z_1 через пробел: '))
            z_2 = Calculation(input('Введите веществ. и мним. часть компл. числа z_2 через пробел: '))
            print(z_1 + z_2)
            print(z_1 * z_2)
        except (ValueError, IndexError):
            print('Ошибка! Повторите ввод')
            input_num()
    input_num()
