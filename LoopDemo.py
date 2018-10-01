#Loops are structures used to repeat sections of code.
#They are useful if you have to do the same thing more than once
#or you can establish a pattern

#This is a counted loop. I want you to think about 
#count, check, change
#i = 0, 0 < 5, TRUE - RUN LOOP

for i in range(-21,47,1):
	print(i*2)

print("****BACKWARDS****")

for i in range(10,-1,-1):
	print(i)



print("MOVING ON")

print("*****Printing String Characters*****")
str = "MONKEY"
for i in range(len(str)-1,-1,1):
	print(str[i])

credit