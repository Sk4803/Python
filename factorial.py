def fact(n) :
    if n < 2 :
        return 1
    return n*fact(n-1)

#_main_
n = int(input("Enter a number (>0) :"))
print("Factorial of", n, "is", fact(n))
