//Hello
n= int(input("Enter the number of entries :"))
l1 = []
for i in range(1, n+1) :
    x = int(input("Enter the number :"))
    l1.append(x)
l1.sort()
print("Entries in ascending order is :")
for a in l1 :
    print(a)
    
    
