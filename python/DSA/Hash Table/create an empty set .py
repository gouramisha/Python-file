#Create an Empty Set
my_list = [None, None, None, None, None, None, None, None, None, None]

# Create an empty list (it can also be a dictionary or a set).
# Create a hash function.
# Inserting an element using a hash function.
# Looking up an element using a hash function.
# Hand ling collisions.

# Create a Hash Function
def hash_fundtion(value):
    sum_of_cars = 0
    for char in value:
        sum_of_chars =+ord(char)

        return sum_of_chars % 10 
    print(" 'Bob' has hash code :", hash_fubction('Bob'))

#Insert an Elemment
def add(name):
 def hash_fundtion(value):
    index = hash_function(name)
    my_list[index] = name

add('Bob')
print(my_list)

# Looking up a name
def contains(name):
  index = hash_function(name)
  return my_list[index] == name

print("'Pete' is in the Hash Table:", contains('Pete'))