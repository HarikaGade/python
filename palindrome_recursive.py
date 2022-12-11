#palindrome by recursive ?
def chk_palindrom(s):
    if len(s)>1:
        return True
    elif s[0]==s[1]:
        return chk_palindrom(s[1:-1])
    else :
        return False
s=input("Enter  any str:")
if chk_palindrom==True:
    print("str is palidrome")
else :
    print("str is not palindrome")
    
