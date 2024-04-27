def is_leap(year):
    leap = False
    if(1900 <= year <=10**5):
        if(year/4==year//4):
            leap = True
            if(year/100==year//100):
                leap=False
                if(year/400==year//400):
                    leap = True 
    return leap

print(is_leap(2000))
print(is_leap(2011))
print(is_leap(2032))
