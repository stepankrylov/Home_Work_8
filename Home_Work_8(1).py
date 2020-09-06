from datetime import date


class Date:
    def __init__(self):
        pass

    @classmethod
    def extract_date(cls, d):
        extract_data = [int(i) for i in d.split('-')]
        return f'День: {extract_data[0]}\n' \
               f'Месяц: {extract_data[1]}\n' \
               f'Год: {extract_data[2]}'

    @staticmethod
    def valid_date(d):
        extract_data = [int(i) for i in d.split('-')]
        try:
            date(extract_data[2], extract_data[1], extract_data[0])
            return f"Валидация даты '{d}' прошла успешно"
        except ValueError:
            return f"Валидация даты '{d}' не пройдена"


if __name__ == '__main__':
    data = '29-02-2020'
    res = Date()

    print(res.extract_date)
    print(f"Результат вызова через экземпляр:\n"
          f"{res.extract_date(data)}\n"
          f"Результат вызова через класс:\n"
          f"{Date.extract_date(data)}")

    print(res.valid_date)
    print(f"Результат вызова через экземпляр:\n"
          f"{res.valid_date(data)}\n"
          f"Результат вызова через класс:\n"
          f"{Date.valid_date(data)}")
