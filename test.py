n = 100# = > we are assigning something
# if n < 100: # now if I want to check wether n has 100 or not [== ]
#   print("It is less than")
# else:
#   print("It's not ") # this condition will only work if above condition is not true
n = int(input("Enter the number: ")) #take input from user
n <= 100 #we will add < sign 
if n < 100:
  print("It is less than!")
else:
  print("It's not")


# Q4. Write a program to check whether a person is eligible for voting or not. (accept age from user)
# # Show Answer
n = int(input("Enter your age: "))
if n >= 18:
  print("Eligible for voting")
else:
  print("Not eligible for voting")

# n = int(input("Enter your number : "))
# if n %2 ==0: # if I divide the number by 2 
#    print("Number is even")
# else:
#   print("Number is Odd")
n = int(input("Enter your number: "))
if n % 2 == 0:
  print("Number is even!")
else:
  print("Number is odd!")


# n = 20
# j = 31
# if n ==20 or j ==30: # and both conditions have to be true
# # OR one of the condition have to be true
#   print("Hello")
# else:
#   print("BAyyi")
#OUTPUT will be "Hello"
n=20
j=31
if n==20 and j==30: #if we want both the conditions have to be true  we will use and logical operator instead of or
  print("Hello")
else:
  print("Bayyi")
# OUTPUT will be "Bayii"

#Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.
n = int(input("Enter a number form 1 to 7: "))
if n==1:
  print("Sunday")
elif  n==2:
  print("Monday")
elif n==3:
  print("Tuesday")
elif n==4:
  print("Wednesday")
elif n==5:
  print("Thursday")
elif n==6:
  print("Friday")
elif n==7:
  print("Saturday")
else:
  print("Invalid number")

# this means I am storing 20 as data inside num1 
# = > is used to store something

# == > to check if num1 has 20 or not
num1=20
if num1==20:
  print("num1 has the value 20!")
else:
  print("num1 does not have the value 20!")

# Accept any city from the user and display monument of that city.
#                   City                                 Monument
#                   Delhi                               Red Fort
#                   Agra                                Taj Mahal
#                   Jaipur                              Jal Mahal
a = (input("Enter city: "))
if(a == "Delhi"):
  print("Red fort")
elif(a == "Agra"):
  print("Taj mahal")
elif(a == "Jaipur"):
  print("Jal mahal")