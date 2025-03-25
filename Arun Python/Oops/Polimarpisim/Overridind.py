class A:
    a=10
    def ride(self):
        print("In side the class A")
class B():
    a=20
    def ride(self):
        print(" In side the Class B")
obj=B()
print(obj.a)
obj.ride()