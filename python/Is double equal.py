a = [1, 2, 3]     # Chocolate box 1
b = [1, 2, 3]     # Chocolate box 2 (same type ki chocolate, alag box me)

print(a == b)     # Haan! Dono chocolates same taste ki hain → True
print(a is b)     # Nahi! Yeh dono alag boxes hain → False

c = a             # c ne wahi chocolate box uthaya jo a ke paas hai
print(a is c)     # Haan! Dono same chocolate hain → True
