'''
#have user enter inveestment amount and expected interest
#each year investment increase by their investment increase by (investment*interest)
#print out earnings after 10 years'''
my_float =input("enter your investment amount: ")
interest = input("enter interest rate:")
my_float=float(my_float)
interest=float(interest)* .01
for i in (range(10)):
    my_float = my_float + (my_float * interest)
print("compound interest after 10 years investment:{:.2f}".format(my_float ))
