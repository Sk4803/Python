num = int(input("Enter a number :"))
sum1 = 1
temp = num
while temp > 1 :
    sum1 *= temp
    temp -= 1
print("Factorial of", num, "is", sum1 )
