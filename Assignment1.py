#1 Write a Python program to print the following string in a specific format


print("Twinkle, twinkle, little star,\n" +
       "     How I wonder what you are!\n" +
       "           Up above the world so high,\n" +
       "           Like a diamond in the sky.\n" +
       "Twinkle, twinkle, little star,\n" +
        "     How I wonder what you are")

#2. Write a Python program to get the Python version you are using print
import sys
print(sys.version)
 
#3. Write a Python program to display the current date and time.
import datetime
print("current date & time: " , datetime.datetime.now())

#4.Write a program which accepts the radius of a circle from the user and compute the area.
radius =int(input("Enter the radius = "))
area = 3.14159265359 * (radius**2)
print("for radius = "+ str(radius) + " area is = " + str(area))

#5. Write a Python program which accepts the user's first and last name and
#print them in reverse order with a space between them.
fname= input("enter your first name ")
lname= input("enter your last name ")
print(lname +" "+ fname)

#6. Write a python program which takes two inputs from user and print them addition
a= int(input("Enter the first value "))
b= int(input("Enter the second value "))
c= a+b
print("addition = " + str(c))
