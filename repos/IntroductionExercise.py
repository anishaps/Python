english = float(input("Please enter your English marks: "))
maths = float(input("Please enter your Maths marks: "))
science = float(input("Please enter your Maths marks: "))

total = english + maths + science
average = total / 3
percentage = (total / 300) * 100

print("\nTotal Marks = %.2f" %total)
print("Average Marks = %.2f" %average)
print("Marks Percentage = %.2f" %percentage)
