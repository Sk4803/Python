//armstrong number
num = int(input("Enter a number :"))
sum1 = 0
l = []
temp = num
order = 0
while temp > 0 :
    digit = temp%10
    l.append(digit)
    temp = temp//10
    order += 1
for i in l :
    i = i**order
    sum1 += i
if num == sum1 :
    print(num, "is an Armstrong number.")
else :
    print(num, "is not an Armstrong number.")
