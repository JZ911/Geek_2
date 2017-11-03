def hello():
    """нічого особого в цих функціях немає"""
    print('hi')
def color(a='withe',b='blue'):
    print(a)
    print(b)
def math(a=input('перше число:'),b= input('друге число:'),s=input('znak')):
   if s == '+':
    print(a + b)

def main ():
    hello()
    color()
    math()
main() # тут все зрозуміло)))