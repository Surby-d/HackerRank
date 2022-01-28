def dayOfProgrammer(year):
    l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daytot=month=theday=0
    for i in l:
        if daytot + i < 256:
            daytot += i
            month += 1

    if year==1918:
        theday = 256 - (daytot-13)


    elif year<1918:
        if year%4==0:
            theday = 256 - (daytot + 1)

        else:
            theday = 256 - daytot

    elif year>1918:
        if (year%400==0) or (year%4==0) and (year%100!=0):
            theday = 256 - (daytot+1)

        else:
            theday = 256 - daytot



    print("{0}.0{1}.{2}".format(theday, month + 1, year))



year = int(input())
dayOfProgrammer(year)
