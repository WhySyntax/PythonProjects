while True:
    try:
        date1 = input("choose your 1st date in the form XX-XX-XXXX\n")
        month1 = int(date1[0:2])
        day1 = int(date1[3:5])
        year1 = int(date1[6:])
        if month1 < 13 and day1 < 32:
            break
        else:
            print("use valid dates")
    except ValueError:
        print("do it properly")
while True:
    try:
        date2 = input("choose your 2nd date the form XX-XX-XXXX\n")
        month2 = int(date2[0:2])
        day2 = int(date2[3:5])
        year2 = int(date2[6:])
        if month2 < 13 and day2 < 32:
            break
        else:
            print("use valid dates")
    except ValueError:
        print("do it properly")
print("calculating later date")
if year1 > year2:
    print("Your first date is after your second one")
elif year2 > year1:
    print("Your second date is after your first one")
else:
    print("your years are the same")
    if month1 > month2:
        print("Your first date is after your second one")
    elif month2 > month1:
        print("Your second date is after your first one")
    else:
        print("your months are the same")
        if day1 > day2:
            print("Your first date is after your second one")
        elif day2 > day1:
            print("Your second date is after your first one")
        else:
            print("both your dates are the same")