class A:
    def __init__(self):
        print("Inside the __init__ method of class A")
class B(A):
    def __init__(self):
        super().__init__()
        print("Inside __init__ the method of class B")
B()