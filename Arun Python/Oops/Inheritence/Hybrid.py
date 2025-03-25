class A:
    a=1
class B(A):
    b=2
class C(A):
    c=3
class D(B,C):
    d=4
obj=D
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)
