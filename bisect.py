import bisect
l = [10, 20, 30, 40, 50, 60, 80, 70]
l.sort()
print("The list in sorted order is :")
print(l)
Item = int(input("Enter new element to be inserted :"))
ind = bisect.bisect(l, Item)
bisect.insort(l, Item)
print (Item, "inserted at index ", ind)
print("The list after inserting new element is :", l)
