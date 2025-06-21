def calculate(para,num1,num2):
    switch = {
        1:num1+num2,
        2:num1-num2,
        3:num1*num2,
        4:num1/num2,
        5:num1**num2,
        6:num1%num2,
        7:num1//num2,
    }
    return switch.get(para,"nothing")

num1 = float(input("Enter first Number: "))
num2 = float(input("Enter second Number: "))
print()
print('''Choices Available:
      1. Add
      2. Subtract
      3. Multiply
      4. Divide
      5. Exponential
      6. Modulus
      7. Floor Division\n''')
choice = int(input("Enter your Choice: "))
print(calculate(choice,num1,num2))
