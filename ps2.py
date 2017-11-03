def print_info (object="monitor",color="white", price="100$"): #задані аргуименти
    """"функція для виводу інформації"""
    print ("function called")
    print("objeckt:", object, sep='\t') #sep='\t це розділити і табуляція
    print("color:", color, sep= '\t')
    print("price", price, sep= '\t')

print_info("keyboard","black", "20$") #заміна аргументів
print()
print_info(object="mouse", color="orange", price="10$")
print()
print_info(color="black")
print()
print_info()
#help(print_info)