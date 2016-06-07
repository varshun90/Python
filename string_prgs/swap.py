def main():
    str=list(input("Enter srting 1: "))
    noOfSwaps = 0 
    if len(str)%2==0:
        noOfSwaps=len(str)/2
    else:
        noOfSwaps=(len(str)/2)-0.5
    
    for i in range(0,int(noOfSwaps)):
        temp = str[i]
        str[i]=str[len(str)-1-i]
        str[len(str)-1-i]=temp
        print("reverse string value is ", "".join(str))
main()
    
    
