#Basic - Print all integers from 0 to 150
for number in range(151):
    print(number)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5,1001,5):
    print(i)

#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1,101):
    print(i)
    if i % 5 == 0 and i % 10 == 0:
        print("Coding,Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
        
#Add odd integers from 0 to 500,000, and print the final sum.

minimum = int(0) 
maximum = int(500000)
Oddtotal = 0

for number in range(minimum, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from {} to {} = {}".format(minimum, maximum, Oddtotal))

#Print positive numbers starting at 2018, counting down by fours.
countdown = 2018

for count in range(countdown, 0, -4):
    print(count)


#Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum,
#print only the integers that are a multiple of mult. 
#For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lownum = 2
highnum = 9
mult = 3

for number in range(lownum, highnum):
    if(number %3 == 0):
        print(number)







