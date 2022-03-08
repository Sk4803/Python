def FindPos (Ar, item) :
   size = len(Ar)
   if item < Ar[0] :
      return 0
   else :
      pos = -1
   for i in range(size-1) :
      if (Ar[i] <= item and item < Ar[i+1]) :
         pos = i+1
         break
      if (pos == -1 and i <= size-1) :
         pos = size
      return pos

def Shift (Ar, pos) :
   Ar.append(None)
   size = len(Ar)

   i = size-1
   while i >= pos :
      Ar[i] = Ar[i-1]
      i =i-1

#_main_
l = [10, 20, 30, 40, 50, 60, 70]
print("The list in sorted order is :")
print(l)
ITEM = int(input("Enter new element to be inserted :"))
position = FindPos(l, ITEM)
Shift(l, position)
l[position] = ITEM
print("The list after inserting:", ITEM, "is :")
print(l)
