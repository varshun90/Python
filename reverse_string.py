def main():
    str1=input("Enter srting 1: ")
    str2=""
    for i in range(len(str1)-1, -1, -1):
         str2=str2+str1[i]
    print("reverse string string value is ",str2)
   # print(str1[::-1])
    
main()
    
    
