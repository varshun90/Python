str1 = input("Enter the value:")
str2 = input("Enter the value:")

if len(str1)==len(str2) and ((sorted(str1)) == (sorted(str2))):
    print("Order and charecters of str1 and str2 are equal,its an anagram")

else:
    print("Not an anagram")



