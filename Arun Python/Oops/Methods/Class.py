####Example1
# class new():
#     def fun1(self):
#       pass
#
#     def fun2(self):
#         print("Second function")
# mc1=new()
# mc1.fun1()
# mc1.fun2()

####Example2

# class two():
#     def One(self,name):
#         print(name)
#     @staticmethod     #we can call directly using class and in static method self keyword word is not required
#     def two(number):
#         print(number)
# two().two(100)
# a=two()
# a.One("sree")


####Example3

# class A():
#     a,b=2,5
#
#     @staticmethod
#     def three():
#         print(A.a+A.b) #if we want to use class variables inside the functions we need to use self key word
#     @staticmethod
#     def four():
#         print(A.a*A.b)
# A.three()
# A.four()


####Example4

class B():
    def __init__(self):
        print("This is constructor")
    def one(self):
        print("this is method")
mc=B() #invoke constructor automatically
mc.m1()#method we have to call explicitly by using object