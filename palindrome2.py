def isPalindrome(string) :
    l = len(string)
    i = 0
    while i <= l/2 :
        if string[i] == string[-(i+1)] :
            i += 1
            continue
        else :
            return False
    return True
#_main_
string = str(input("Enter a string :"))
print(isPalindrome(string))
