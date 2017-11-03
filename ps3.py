def  print_numbers(limit):
    """"функція яка приймає параметр ліміт, якесь максимальне число """
    for _ in range (limit): # значок _ або і для підрахунку
      print(_)
      print()
      print("hello, world")
def add_numbers(one, two):
    """"функція повертає значення one + two"""
    return one + two
def function(x):
    """функція яка повертає значення якщо відємно то помножено на 2, а в другому випадку множить на 3"""
    if x<0:
       return x*2
    else:
        return x*3

def main():
    """функція яка обєднує 3 попередні"""
    n =int(input("input number"))
    print_numbers (n)
    print()
    resault = add_numbers(1, 2)
    print("my resault",resault)
    print()
    for i in range(-3,4):
        y=function(i)
        print('function(',i, ')=',y, sep='')
main()
#help(main) дізнатися про функцію