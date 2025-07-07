try:
    # code jisme error aa sakta hai
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")


try:
    x = int(input("Enter number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", x)
finally:
    print("Done.")
