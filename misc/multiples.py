'''This program adds multiples of 5 and 3 in a given range'''

def main():
    n=int(input("enter number:"))
    sum1=0
    sum2=0
    for i in range (1,n+1):
        if i%3==0 :
            sum1=sum1+i
        elif i%5==0:
            sum2=sum2+i
    print(sum1+sum2)
        
main()      
