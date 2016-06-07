def num(m,n):
    if(m == 0):
       return n+1
    if(m > 0) and (n == 0):
       return num(m-1,1)
    if(m > 0) and (n > 0):
       return num(m-1,num(m,n-1))
    
if __name__=='__main__':
    x= num(1,1)
    print("num(1,1) = ", x)
    if num(1,1) != 3:
        raise Exception("num(1,1) Failed")
    x= num(0,2)
    print("num(0,2) = ", x)
    if num(0,2) != 3:
        raise Exception("num(0,2) Failed")
    x= num(0,0)
    print("num(0,0) = ", x)
    if num(0,0) != 1:
        raise Exception("num(0,0) Failed")
    x= num(1,0)
    print("num(1,0) = ", x)
    if num(1,0) != 2:
        raise Exception("num(1,0) Failed")
    x= num(-1,-1)
    print("num(-1,-1) = ", x)
    if num(-1,-1) != None:
        raise Exception("num(-1,-1)2:17 PM 12/19/2014 Failed")

    print("Secret Successful")
