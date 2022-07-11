import math

while True:
    oprator = input("Plz enter an Oprator such as (+,-,*,/,sin,cos,tan,cot,Radical,factorial,exit): ")

    if oprator == "exit":
        break
    elif oprator == "+" or oprator == "-" or oprator == "*" or oprator == "/":
        a = int(input("Plz enter a number as a: "))
        b = int(input("Plz enter a number as b: "))
    else:
        a = int(input("Plz enter a number as a: "))

    if oprator == "+":
        result = a + b
    elif oprator == "-":
        result = a - b
    elif oprator == "*":
        result = a * b
    elif oprator == "/":
        if b != 0 :
            result = a / b
        else:
            result = "Can not division by Zero!!"
    elif oprator == "sin":
        result = math.sin(a * 180 / math.pi)
    elif oprator == "cos":
        result = math.cos(a * 180 / math.pi)
    elif oprator == "tan":
        result = math.tan(a * 180 / math.pi)
    elif oprator == "cot":
        result = math.tanh(a * 180 / math.pi)
    elif oprator == "Radical":
        result = math.sqrt(a)
    elif oprator == "factorial":
        result = math.factorial(a)

    print ("result = ", result)
