# Typecasting  in python
#the conversion of one data type into the other data type is known is as type casting.
#  two type of typecasting


# 1. Explicit ConversionSyntax 
# 2. implicit Conversion

a = "1"
b = "2"
print(int(a) + int(b))

# Implicit Typecasting
c = 1.9
d = 8
print (c + d)

a = 31
type(a) # class <int>
b = "31"
type (b) # class <str>A number can be converted into a string and vice versa (if possible)
# There are many functions to convert one data type into another.
str(31) =>"31" # integer to string conversion
int("32") => 32 # string to integer conversion
float(32) => 32.0 # integer to float conversion