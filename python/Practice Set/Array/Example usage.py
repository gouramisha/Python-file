# 2D and 3D Vectors
v3 = Vector3D(1, 2, 3)
print(v3.x, v3.y, v3.z)

# Dog barking
dog = Dog("Tommy")
print(dog.bark())

# Employee salary
emp = Employee(60000)
emp.increment = 0.15  # will set to 0.2 due to salary > 50000
print(emp.salaryAfterIncrement)

# Complex numbers
c1 = Complex(2, 3)
c2 = Complex(1, 4)
print(c1 + c2)
print(c1 * c2)

# Vector addition and dot product
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print((v1 + v2).components)
print(v1 * v2)

# 3D vector string
v3d = Vector3(7, 8, 10)
print(v3d)

# Vector length
vn = VectorN([1, 2, 3, 4])
print(len(vn))
