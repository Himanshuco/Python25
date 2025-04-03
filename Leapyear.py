"""Leap year and Century year calculation"""

year = int(input("Enter a year : "))
if(year%4==0 and year%100!=0) or (year%400==0):
    if(year%100==0):
        print(f"{year} is a leap year and also a century year")
    else:
        print(f"{year} is a leap year but not a century year")
else:
    print(f"{year} is not a leap year")