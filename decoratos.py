def log_decorator(func):
    def wrapper():
        print("Function called!")
        func()
    return wrapper

@log_decorator
def say_hi():
    print("Hi!")

say_hi()



def my_decorator(func):
    def wrapper():
        print("Function se pehle 📢")
        func()
        print("Function ke baad ✅")
    return wrapper

@my_decorator
def say_hello():
    print("Hello Duniya!")

say_hello()


def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print(f"Yeh function {count} baar chala.")
        func()
    return wrapper

@count_calls
def greet():
    print("Namaste!")

greet()
greet()
greet()

