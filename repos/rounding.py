number1 = input("Enter whole number:") 
number2 = input("Enter decimal number:")

int_num = int(number1) # hyp - display number 1 as the integer that was entered
float_num = float(number2) #hyp - display number 2 as it was entered
round_num = int(round(float_num)) #hyp - number 2 rounded to the nearest integer

print(int_num, float_num, round_num) #hyp - number 1, number 2, number 2 to the nearest integer