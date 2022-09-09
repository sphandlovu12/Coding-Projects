
def ageCalc(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days/365.25)
    print("Your age is: ", age)


#y=year m=month d=day
y=int(input("Birth year: "))
m=int(input("Birth month: "))
d=int(input("Birth date: "))
ageCalc(y, m, d)