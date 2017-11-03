def foo(in_str):
    """функція працює і з літерами і з цифрами"""
    if len(in_str) > 50: #якщо довжина довша 50 то згідно пункту 3 в завданні
        print("")
    elif len(in_str) < 30: #якщо менше 30 пункт 2
        s = 0
        new_str = ''
        for ch in in_str:
            if ch.isdigit():
                s += int(ch)
            else:               #а інакше пунк 1
                new_str += ch
        print(s)
        print(new_str)
    else:
        print(len(in_str))
s = input('Ввести строчку_1:')
foo(s)
s = input('Ввести строчку_2:')
foo(s)
s = input('Ввести строчку_3:')
foo(s)
#важке завдання