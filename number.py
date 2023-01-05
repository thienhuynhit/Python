import random as rd
#  there are three numeric types in python
# int float complex
# int or integer,is a whole number, possitve or negative, without decimals,of unlimited length
x=123445
y=-1234567
print(type(x),type(y))

# float
x=2.30
y=-23.123
print(type(x),type(y))
# we can use e 
y=345e2
print(type(y))

# complex number
x=2+3j
y=-5j
print(type(x),type(y))

# conversion types
#  you can convert data type to another by using these methods int(),float(),complex()
x=123
y=234.12
z=12-3j

a=float(x)
b=int(y)
c=complex(z)

print(type(a))
print(type(b))
print(type(c))


# nultiple complex numbers
x=2-3j
y=3+4j
z=x*y
print(z)


# module random
print(rd.randrange(1,20))