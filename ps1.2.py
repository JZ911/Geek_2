months = {1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень', 5: 'Травень', 6: 'Червень', 7: 'Липень', 8: 'Серпень', 9: 'Вересень',
          10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'}


def pecat_mesyaca(n):
    """функція пори року"""
    print(months[n])


while True:
    try:
        pecat_mesyaca(int(input('Введите номер месяца: \n')))
    except:
        break   #програма тотожна 1.3, але трохи спрощенв