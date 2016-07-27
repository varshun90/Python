string1=input("enter string:")
sub_string=input("enter sub_string:")
times=0
for i in range(0,len(string1)):
    if string1[i:i+len(sub_string)]==sub_string:
        times+=1
print(times)
