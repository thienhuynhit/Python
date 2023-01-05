# data types
# we use type() to verify data-type of a variable
# str
x="hello world"
print(type(x))
# int
x=1
print(type(x))
# float
x=2.34
print(type(x))
# complex
x=2+3j
print(type(x))
# list
x=[1,2,3]
print(type(x))
# tuple
x=("banana","mango","orange")
print(type(x))
# range
x=range(5)
print(type(x))
# dict
x={"model":"Volvo","price":20000}
print(type(x))
# set
x={"banana","water-melon"}
print(type(x))
# frozenset
x=frozenset({"coconut","mango"})
print(type(x))
# bool
x=True
print(type(x))
# bytes
x=b"hello"
print(type(x))
# bytearray
x=bytearray(5)
print(type(x))
# memoryview
x=memoryview(bytes(5))
print(type(x))
# NoneType
x=None
print(type(x))

# if you want to specify data type, you can use the following instruction
y=int(2.3)
print(type(y))