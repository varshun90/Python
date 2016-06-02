print("This program was written by Varshini")
year=eval(input('Please enter a Year:'))
month=eval(input('Please enter a Month:'))

def main():    
    if (month > 12 or month < 0):
        print("invalid month")
       
def isleapyear(year):
    
    if year % 400 == 0:
       return True
    elif year % 100 == 0:
       return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
def days_in_month_year(month,year):    
    leapyear=isleapyear(year)
    if (month == 1 or month ==3 or month == 5 or month == 7 or month==8 or month== 10 or month == 12):
        print("There are 31 days in the month of %d of year%d"%(month,year))
    elif(month==4 or month==6 or month==9 or month==11):
        print("There are 30 days in the month of %d of year%d"%(month,year))
    elif(month==2 and leapyear== True):
        print("There are 29days in the month of %d of year %d and it is leap year"%(month,year))
    elif(month==2 and leapyear==False):
        print("there are 28 days in the month of %d of year %d and not a leap year"%(month,year))
    else:
        print("invalid month",month)

days_in_month_year(month,year)

