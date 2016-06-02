

def is_reverse(a):
    b=""
    if len(a)!=len(b):
        print ("this is not palidrome:")
    else:
        for i in range(len(a)-1,-1,-1):
            b=b+a[i]
            return b
        print("reverse of a",b)
    if a==b:
        print("this is a palindrome:")
is_reverse("abba")        
    
