# string in python
# assigning a string to a variable is done with the variable name followed by and equal sign and the string
x="hello world"
print(x)

# you can assign multiline string to a variable by using three quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# string is an array. So you can access a character in an array .
a="hello"
print(a[0])

# looping through a string
for x in "banana":
    print("this is item in string: ",x)

# to get the length of a string, you can use len()
print(len("hello world"))

# check string
#  To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)
if "free" in txt:
  print("Yes, 'free' is present.")

# check if not
txt = "The best things in life are free!"
print("expensive" not in txt)
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# slicing strings
# Get the characters from position 2 to position 5 (not included):
b="hello world"
print(b[2:5])

# slice from the start 0-4
print(b[:5])

# slice to the end 2-end
print(b[2:])

# use the negative index
# Use negative indexes to start the slice from the end of the string
# character of the end of string is -1
x="Hello world!"
print(x[-5:-2])


# modify string
# upper or lower 
# The upper() method returns the string in upper case
a="Hello World!"
print(a.upper())

# The lower() method returns the string in lower case
print(a.lower())

# the strip() method removes any whitespace from the begining or the end of the string
a="  Hello World!   "
print(a.strip())

# The replace() method replaces a string with another string
a = "Hello, World!"
print(a.replace("H","J"))

# split string
# The split() method returns a list where the text between the specified separator becomes the list items.
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# string concatenation
a="Hello"
b="world!"
c=a+" "+b
print(c)

# format string
# we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
age = 30
txt = "My name is Harvey, I am {} years old"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
Myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(Myorder.format(quantity, itemno, price))

# Escape character
txt="They are the last \"Samurais\" in Japan"
print(txt)