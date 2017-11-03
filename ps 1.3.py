months = {1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень', 5: 'Травень', 6: 'Червень', 7: 'Липень', 8: 'Серпень', 9: 'Вересень',
          10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'}

"""тут видно, що аргумет це місяці"""


def season(n):
    """функція пори року"""
    print(months[n])


while True:
    vvod = input('Введіть номер місяця: \n') # програма заключаеться в введенні № місяці і отримати відповідний місяць
    if vvod == '': break
    try:
        season(int(vvod))
    except KeyError:
        print('ЕРОР. потрібно ввести від 1 до 12.')
    except ValueError:
        print('ЕРОР. Потрібно вводити числа, від 1 до 12.')