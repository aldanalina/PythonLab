san1 = int(input("1 san: "))
san2 = int(input("2 san: "))

amal = input()

if amal == '+':
    print("Result:", san1+san2)
elif amal == '-':
    print("Result:", san1-san2)
elif amal == '/':
    if(san2 == 0):
        print("Nolge boluge bolmaidy.")
    else:
        print("Result:", san1/san2)
elif amal == '*':
    print("Result:", san1*san2)
else:
    print("Error")