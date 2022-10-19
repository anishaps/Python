number1 = float(input("Enter first number: ")) 
number2 = float(input("Enter second number: "))

if number1 > number2: #if number1(a decimal) is greater than number2(a decimal) then number1 being bigger is true, if number 1 is not greater then it is false
    number1bigger = True 
else:
    number1bigger = False

print("It is", number1bigger, "that number1 is bigger.") 