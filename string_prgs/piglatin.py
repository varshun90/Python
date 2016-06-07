def main():
    a=input("enter word to be translated:")
    vowels=['a','e','i','o','u']
    if a[0] in vowels:
        print(a+'hay')
    else:
        print(a[1:]+a[0]+'ay')
main()        

