
#name = "bro"
#print("hello " +name)

#age = 21
#age += 1
#print("Your age is : " +str(age))
#print(type(age))

#height = 250.5
#print("Your height is : " +str(height)+ "cm")

#human = False // dont ever put"False" bcs it will became str instead boolean
#print(human)
#human = True
#print("Are you a human : "+str(human))

#multiple assignment

#name = "Bro"
#age = 21
#attractive = True

#Spongebob = Patrick = sandy = squidward = 30

#print(Spongebob)
#print(Patrick)
#print(sandy)
#print(squidward)

#name = "Bro code"
#print(name.find("B"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())/boolean
#print(name.isalpha())
#print(name.count("o")) // to count how many "o"
#print(name.replace("o","a"))// to replace alphabet
#print(name*3) // to make multiple str

#type casting

x = 1 #
y = 2.0 #float
z = "3" #str

#how to change int to float, float to int, float to str
#x = float(x)
#y = int(y)
#z = str(z)

#print("x is " +str(x))
#print(y)
#print(z*3)

#name = input("What is your name? :")
#age = int(input("how old are you ? : "))
#height = float(input("How tall are you ? :"))

#age = age + 1
#print("hello " + name)
#print("you are "+str(age)+" years old")
#print("you are "+str(height)+"cm tall")

#import math
#pi = 3.14
#x = 1
#y = 2
#z = 3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(max(x,y,z)) // to find the largest value
#print(min(x,y,z)) // to find the lowest value

#slicing = create a substring 
#name = "Bro code"

#first_name = name [:3]
#last_name = name[4:]
#funky_name = name[::3]
#reversed_name = name [::-1]

#print(reversed_name)

#website = "https://google.com"

#slice = slice(7,-4)

#print(website[slice])

#if statement

#age = int(input("how old are you? :"))

#if age == 100:
    #print("You are a century old")
#elif age >= 18:
    #print("You are an adult :")

#elif age < 0: // elif is shorcut for else if
    #print("you havent been born yet")
#else:
    #print("You are a child:")   

#LOGICAL OPERATOR
#temp = int(input(" what is the temperature outside? :"))

#if temp>= 0 and temp <= 30:
 #   print("The temperature is good today")
  #  print("Go oustide")
#elif  temp < 0 or temp >30:
 #   print("The temperature is bad todAY")
  #  print("stay inside")


#while loop

#name = None
#while not name :
 #   name = input("Enter your name :")
#print("hello "+name)

#FOR LOOP

#for i in range(10):
 #   print(i)

#for i in range(50,100+1,2):
 #   print(i)

#for i in "bro code":
 #   print(i)

#NESTED LOOP

#rows = int(input("how many rows?"))
#columns = int(input("how many colummns? "))
#symbol = input("Enter a symbol to use : ")

#for i in range (rows):
 #   for j in range (columns):
  #      print(symbol, end="")
   #     print()

#LOOP 

#while True:
 #   name = input("Enter your name : ")
  #  if name != "":
   #     break   

#phone_number = "123-456-7890"

#for i in phone_number:
 #   if i == "-":
  #      continue
   # print(i, end="")

#for i in range(1,21):
 #   if i == 13:
  #      pass
   # else:
    #    print(i)

#Thomas_age = 3
#Age_at_Kindergarden = 5

#if Thomas_age < Age_at_Kindergarden:
 #   print("Thomas should be in pre-school")
#elif Thomas_age == Age_at_Kindergarden:
 #   print("Enjoy kindergarden ")   
#else:
 #   print("Thomas should be in another class")

#x=0
#while(x<5):
 #   print(x)
  #  x=x+1

#for x in range (5,10):
 #   print(x)

#days=["Mon","Tue","Wed","Thu","Fri","sat","sun"]

#for d in days:
 #   if(d=="Thu"):
  #      continue
   # print(d)

i = 1
while i<= 5 :
    print(i * '*')
    i = i + 1

numbers =[1,2,3,4,5]
for item in numbers:
    print(item)
    
if gred > 80 :
    print("You are briliant")
else :
    print("Better luck next time")

mark = int(input("How much mark did you get ?"))





