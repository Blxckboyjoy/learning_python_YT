#!/usr/bin/python3

'''
#problem : recieve miles ad convert to KM
#KM = M * 1.60934
#enter miles %
# 5 miles equal 8.04 KM
'''
miles = input('enter miles\t')
miles = int(miles)
km = miles * 1.60934
print("{}miles are equal to {} kilometers".format (miles, km))

