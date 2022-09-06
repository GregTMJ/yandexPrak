import datetime as dt


class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount

        # Нужно определиться какого типа должен быть self.date, здесь мы получаем тип tuple
        # Лучше ставить логику в одну линию, чтобы лучше понять чему будет равен self.date
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        # При каждом вызове get_today_stats, переменная today_stats обнуляется... (смотреть продолжение ниже)
        today_stats = 0
        # Из хорошей практики лучше всего вызвать переменную, который не имеет схожесть с уже объявленной переменной
        # Тут речь идёт о Record (уже объявлен выше как класс), можно использовать record.
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                # ... тут вы хотите добавить к today_stats некое число и отследить переменную дальше. Если такова ваша
                # глобальная идея, то лучше инициировать эту переменную в самом конструкторе.
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        # Такая же ситуация тут как с get_today_stats и today_stats (смотреть выше)
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            # Можно убрать скобки начальные, и логику разместить на одну строчку
            if (
                    (today - record.date).days < 7 and
                    (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        x = self.limit - self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        else:
            # Можно убирать скобки
            return ('Хватит есть!')


class CashCalculator(Calculator):
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    # Здесь можно поместить курс в конструктор класса, если есть опасение, что курс меняется постоянно.
    # Схожесть аргумента с переменной USD_RATE и EURO_RATE
    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        # Нет надобности помещать аргумент в переменной, можно свободно им пользоваться в методе
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            # Так вы хотите вызвать логику if cash_remained равен 1.00
            cash_remained == 1.00
            currency_type = 'руб'
        if cash_remained > 0:
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    # Здесь наследуется метод и не меняется или добавляется, поэтому можно исключить такое наследование
    def get_week_stats(self):
        super().get_week_stats()


# Всегда в конце оставляйте рабочий пример всего своего кода, чтобы быть полностью уверенным в его работоспособность.
# Можно брать пример из задания.
# Не забывайте про if __name__ == "__main__"

