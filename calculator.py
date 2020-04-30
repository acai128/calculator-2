"""CLI application for a prefix-notation calculator."""

"""
repeat forever:
    read input
    tokenize input
        if the first token is "q":
            quit
        else:
            (decide which math function to call based on first token)
            if the first token is 'pow':
                  call the power function with the other two tokens
"""
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )



while True: 
    equation = input('Enter equation') #+ 2 2
    split_equation = equation.split(' ')
    operation = split_equation[0]
    num1 = split_equation[1]
    num2 = split_equation[2]
    
if split_equation == 'q':
    print('End')

elif operation == "+":
    print(add(num1, num2))

elif operation == "-":
    print(subtract(num1, num2))

elif operation == "*":
    print(multiply(num1, num2))

elif operation == "/":
    print(divide(num1, num2))

elif operation == "square":
    print(square(num1))

elif operation == "cube":
    print(cube(num1))

elif operation == "power":
    print(power(num1, num2))    

elif operation == "mod":
    print(mod(num1, num2))