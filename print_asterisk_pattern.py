# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

for asterisk in range(6,0,-1):
    for i in range(asterisk):
        print(asterisk, end=" ")
    print()