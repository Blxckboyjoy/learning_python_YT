'''nt ine tree and height based on user input

use 1 while loop and 3 for loops


4 spaces 1 hash
3spaces 3 hashes
2 spaces 5 hash
1 space 7 hash
0 spaces 9 hash

1.decrement spaces by 1 each time through loop
2.increment hashes by 2 each time through loop
3.save spaces to the stump by calculating tree height -1
4decrement from tree height until reaches 0
5.print spaces and then hashes for each row
6.print stump spaces and add one hash
'''
treeL= input("enter height of tree: ")
treeL= int(treeL)
spaces = treeL - 1
hash = 1
stumps= treeL -1
while treeL != 0:
    for i in (range(spaces)):
        print(' ',end="")
    for i in (range(hash)):
        print(' ',end="")
        print()
        spaces  -=1
        hash += 2
        treeL -=1
for i in (range(stumps)):
    print(' ',end="")
print("#")



