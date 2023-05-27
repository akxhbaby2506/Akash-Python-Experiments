def is_leap(year):
    leap = True
    if (year%4==0) and (year%100!=0 or year%400 == 0):
        print(year,"is a Leap year")
    else:
        print(year,"is Not a Leap year")
is_leap(1990)
is_leap(2000)