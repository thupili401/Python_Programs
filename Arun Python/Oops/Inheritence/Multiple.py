class A:
    a=1
class B:
    b=2
class C(A,B):
    c=3
obj=C
print(obj.a)
print(obj.b)
print(obj.c)