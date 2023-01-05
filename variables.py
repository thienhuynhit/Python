# this is second lab that help you work with variable in python
# python has no command for declaring a variable 
x="this is new paper"
y=30
print("the first statemant you can express in front of cousin is ",x,"I am ",y,"years old")
# if you want to specify data type of a variable, with can be done with casting
a=str(3)
b=int(12)
c=float(123) 
print(a,b,c)

# if you want to check the data type of a variable 
print(type(a))
print(type(""))

if(type(a)==type("")):
    print("A variable is a string")
else:
    print("please check the str class")

# we will talk about how to a correct name of a variable
# you can sign a value to a variable and re-sign a new value

# there are some rules for giving a variable name:
# 1. the name of a variable must start with a letter a-z
# 2. a variable name cannot start with a number
# 3. a variable name only contains alpha-numeric characters and underscores(a-Z,_)
# 4. variable names are case-sensitive (age, Age and AGE are three different variables)

# there are several techniques,you can use to make them readable.
# 1. Camel Case: each word starts with a capital letter, except the first.
# example: myFullName="Harvey"
# 2. Pascal Case: each word must start with capital letter.
# ex: FullName="Huynh"
# 3. Snake Case: each word is seprated by an underscore.
# ex: full_name="Harvey Huynh"
myFirstName="Harvey"
MyLastName="Huynh"
my_full_name=myFirstName+" "+MyLastName
print(my_full_name)


# assign multiple values
myAvgScore=MyAvgScore=my_avg_score=8.0
if(my_avg_score>=7):
    print("congratulation!! you got the high score")

# assign many values to multiple variables
employee_name,salary="Hung",123
print("my name is ",employee_name," and i got a job with ",salary," USD/Per month")

# if you have a collection of values in a list, tuple,etc. Python allows you to extract the values into variables
fruits=["mango","orange","banana"]
firstFruit,secondFruit,thirdFruit=fruits
print(firstFruit,secondFruit,thirdFruit)


# global variable
x="hello world"
def myFunction():
    # if you define a new variable name with the same name with global variable inside a function. It will be local and you only can use it inside the function. And global variable will remain the value it was.
    x="xin chao"
    print(x)
myFunction()
print(x)

# to change value of a global variable inside a function. refer to global variable by using keyword global
y="welcome to Vietnam"
def sayHello():
    global y
    y="becoming a senior developer is fantastic"
    print(y)

sayHello()
print(y)