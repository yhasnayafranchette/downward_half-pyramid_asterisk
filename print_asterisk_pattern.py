# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

rows = 5

for asterisk in range(rows,0,-1):
    for i in range(0,asterisk):
        print("*", end=" ")
    print()