class A:
    def m1(self):
        print("Clas A")
class B(A):
    def m1(self): 
        print("clas B")
        super().m1()
var =B()
var.m1()