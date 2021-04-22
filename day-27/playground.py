def add(*args):
    print(args) # tuple
    sum = 0
    for arg in args:
        sum += arg

    return sum

print(add(3, 5, 6))

def calculate(n, **kwargs):
    print(kwargs) # dictionary
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    return n

print(calculate(2, add=3, multiply=10))

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        # if not give "model" argument, using the property will crash
        # self.model = kwargs["model"]



car = Car(make="Nissan")
print(car.model)