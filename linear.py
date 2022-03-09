lst = [2, 4, 6, 8, 10]
n = int(input("Enter no. to be searched for :"))
l = len(lst)
for i in range(0, l) :
   if lst[i] == n :
      print (n, "is found at index", i )
