# 1. Приветствие
# 2. Мануал – как пользоваться программой и какие валюты доступны
# 3. Ввести исходную валюту
# 4. Ввести в какую валюту перевести
# 5. Количество валюты
# 6. Подсчёт
# 7. Вывод результата

import online_requests

CURRENCIES = online_requests.get_actual_currencies()


def convert(amount, from_currency, to_currency, currencies):
    from_value = currencies.get(from_currency)  # CURRENCIES[current_currency]
    to_value = currencies.get(to_currency)

    coefficient = to_value / from_value
    return round(amount * coefficient, 2)


def is_currency_in_dict(currency, currencies):
    if currency in currencies:
        return True
    return False

# 1
print("Добро пожаловать в конвертатор валют!")

# 2
print("""
Инструкция:
1. Ввести исходную валюту
2. Ввести результирующую валюту
3. Ввести количество валюты
""")

print("Доступные валюты:")

for key in CURRENCIES:
    print(f'* {key}')

# 3
current_currency = input("Введите исходную валюту: ")
while not is_currency_in_dict(current_currency, CURRENCIES):
    current_currency = input("Данная валюта не поддерживается. Введите исходную валюту из списка: ")

# 4
result_currency = input("Введите результирующую валюту: ")
while not is_currency_in_dict(result_currency, CURRENCIES):
    result_currency = input("Данная валюта не поддерживается. Введите исходную валюту из списка: ")
# 5
amount = input("Введите количество: ")

# 6
result = convert(float(amount), current_currency, result_currency, CURRENCIES)

print(f'{amount} {current_currency} = {result} {result_currency}')
