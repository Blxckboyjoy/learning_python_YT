#if age 5 got to kindergarden
#age 6--17 grades 1-12
#age greater than 17 college
#60 retirement
age = eval(input('enter age: '))
if (age >= 6) and (age <= 17):
    grade = age -5
    print("go to {} grade".format(grade))
if (age == 5):
    print("go to kindergarden")
elif (age <= 5):
    print("too young for kindergarden")
if (age >= 17) and (age >=50):
    print("goes to college")
if (age >=59):
    print("retire bruv")