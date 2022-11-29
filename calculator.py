#!/usr/bin/python3
'''
check if ages are important
1-18 -> important
21,50 -> 65 important
all others not important

recieve age and save in var called age
if age is both gretaer tthan or equal to 1 and less than or equal to 18 important
if age 21 or 50 important
check if age less than 65 then convert T or F and vice versa
else not important
and if both true return true
or idf either true then true
not conver true to false'''
age = eval(input('enter age: '))
if (age >= 1) and (age <= 18):
    print("Important Birthday")

elif (age == 21) or (age == 50):
    print("Important Birthday")

elif not(age < 65):
    print("Important Birthday")

else:
    print("Sorry not Important Birthday")

