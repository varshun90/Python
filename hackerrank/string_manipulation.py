string=input("enter string:")
l=list(string)
i=(int(input("input index:")))
letter=input("Enter letter to be replaced:")
l[i]=letter
string=''.join(l)
print(string)

