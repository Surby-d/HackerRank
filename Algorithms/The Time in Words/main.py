def words(n):
    num2words1 = {0: "Zero", 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
    num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty']
    if n >= 1 and n <= 19:
        return num2words1[n].lower()
    else:
        tens = num2words2[(n//10)-2]
        ones = num2words1[(n%10)]
        return "{0} {1}".format(tens, ones).lower()


nh = int(input())
nm = int(input())
if nm==0:
    print("{0} o' clock".format(words(nh)))
elif nm<=30:
    hour = words(nh)
    minutes = words(nm)
    if nm==15:
        print("quarter past {0}".format(hour))
    elif nm==30:
        print("half past {0}".format(hour))
    else:
        print("{0} minute past {1}".format(minutes, hour) if nm == 1 else "{0} minutes past {1}".format(minutes, hour))
else:
    hour = words(nh+1)
    minutes = words(60-nm)
    if nm == 45:
        print("quarter to {0}".format(hour))
    else:
        print("{0} minute to {1}".format(minutes, hour) if nm == 1 else "{0} minutes to {1}".format(minutes, hour))



