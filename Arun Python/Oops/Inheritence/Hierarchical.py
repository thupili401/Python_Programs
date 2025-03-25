class A:
    a=1
class B(A):
    b=2
class C(A):
    c=3
obj=C
print(C.a)
print(C.c)
obj=B
print(obj.a)
print(obj.b)