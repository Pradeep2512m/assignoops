def multiply(func):
    print("execute this first")
    def insert(a, b):
        print(a)
        print(b)
        return func(a, b)
    return insert
@multiply
def mul(a, b):
    print(a*b)
mul(5, 8)