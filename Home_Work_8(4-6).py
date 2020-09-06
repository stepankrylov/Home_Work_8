class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Stock:
    def __init__(self, name, label):
        try:
            if isinstance(name, str) and isinstance(label, str):
                self.name = name
                self.label = label
            else:
                raise OwnError("Атрибут name и label должны быть типа str!")
        except OwnError as err:
            print(err)

    def receiving(self, r_count, price):
        try:
            if isinstance(r_count, int) and isinstance(price, int):
                try:
                    r_dict = {'Тип': self.name, 'Марка': self.label, 'Кол-во': r_count, 'Стоимость': price}
                    print(r_dict)
                    return f'На склад отгружено {r_count} {self.name}(-а, -ов) марки {self.label} по {price} руб. за шт.'
                except AttributeError:
                    return 'Атрибут name и/или label не определены'
            else:
                raise OwnError("Атрибут r_count и price должны быть типа int!")
        except OwnError as err:
            print(err)

    def delivery(self, division, d_count):
        try:
            if isinstance(division, str) and isinstance(d_count, int):
                try:
                    d_dict = {'Тип': self.name, 'Марка': self.label, 'Кол-во': d_count, 'Подразделение': division}
                    print(d_dict)
                    return f'Со склада в {division} отправлено {d_count} {self.name}(-а, -ов) марки {self.label}'
                except AttributeError:
                    return 'Атрибут name и/или label не определены'
            else:
                raise OwnError("Атрибут division должен быть типа str и price должен быть типа int!")
        except OwnError as err:
            print(err)


class OfficeEq(Stock):
    def __init__(self, name, label):
        super().__init__(name, label)


class Printer(OfficeEq):
    def __init__(self, name, label, p_speed):
        super().__init__(name, label)
        try:
            if isinstance(p_speed, int):
                self.p_speed = p_speed
            else:
                raise OwnError("Атрибут p_speed должен быть типа int!")
        except OwnError as err:
            print(err)

    @property
    def print_speed(self):
        try:
            return f'Скорость печати {self.name}а {self.label} составляет {self.p_speed} стр. в мин.'
        except AttributeError:
            return 'Атрибут p_speed не определен'


class Scanner(OfficeEq):
    def __init__(self, name, label, s_speed):
        super().__init__(name, label)
        try:
            if isinstance(s_speed, int):
                self.s_speed = s_speed
            else:
                raise OwnError("Атрибут s_speed должен быть типа int!")
        except OwnError as err:
            print(err)

    @property
    def scan_speed(self):
        try:
            return f'Скорость печати {self.name}а {self.label} составляет {self.s_speed} стр. в мин.'
        except AttributeError:
            return 'Атрибут s_speed не определен'


class Copier(OfficeEq):
    def __init__(self, name, label, c_speed):
        super().__init__(name, label)
        try:
            if isinstance(c_speed, int):
                self.c_speed = c_speed
            else:
                raise OwnError("Атрибут c_speed должен быть типа int!")
        except OwnError as err:
            print(err)

    @property
    def copy_speed(self):
        try:
            return f'Скорость печати {self.name}а {self.label} составляет {self.c_speed} стр. в мин.'
        except AttributeError:
            return 'Атрибут c_speed не определен'


if __name__ == "__main__":
    stock = Stock('сканер', 'HP')
    print(stock.receiving(4000, 10))
    print(stock.delivery('1-й отдел', 2))
    p = Printer('принтер', 'Epson', 50)
    print(p.print_speed)
    s = Scanner('сканер', 'HP', 40)
    print(s.scan_speed)
    c = Copier('копир', 'Xerox', 45)
    print(c.copy_speed)
