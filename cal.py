operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
a = eval(input('Enter your first number: '))
b = eval(input('Enter your second number: '))

if operation == '+':
    print(a+b)

elif operation == '-':
    print(a-b)

elif operation == '*':
    print(a*b)

elif operation == '/':
    print(a/b)

else:
    print('You have not typed a valid operator, please run the program again.')
