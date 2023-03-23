# What is the function of this line of code?
# Response: Select the highest number from the ten numbers you randomly selected, then print it.

#Import libraries. 
#Randint lets you to choose a random integer; for example, randint(1,5) selects a value between 1 and 5.

from random import randint

# Thhe ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
stored_random_number=0
while progress<10:
	progress+=1
	n = randint(1,100)
	if n > stored_random_number:
		stored_random_number = n

print(stored_random_number)
