# Built-in Data Types


# text type: str
text = 'Hello, World!'
print("text type: ", text)


# number types: int, float, complex
a = 5
b = 5.0
c = 5 + 3j
print("number types: ", a, b, c)

# sequence types: list, tuple, range
list = [1, 2, 3]
tuple = (1, 2, 3)
range = range(10)
print("sequence types: ", list, tuple, range)

# mapping type: dict
dict = {'name': 'Etn', 'age': 10}
print("mapping type: ", dict)

# set types: set, frozenset
set = {1, 2, 3}
frozenset = frozenset({1, 2, 3})
print("set types: ", set, frozenset)

# boolean type: bool
bool = True
print("boolean type: ", bool)

# binary types: bytes, bytearray, memoryview
bytes = b"Hello"
bytearray = bytearray(5)
memoryview = memoryview(bytearray)
print("binary types: ", bytes, bytearray, memoryview)

# None type: None
none = None
print("None type: ", none)


# Getting the Data Type
print(type(text))
print(type(a))
print(type(list))
print(type(memoryview))
print(type(none))