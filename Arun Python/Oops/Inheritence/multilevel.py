class A:
    a=1
class B(A):
    b=2
class C(B):
    c=3
obj=C()
print(obj.a)
print(obj.b)
print(obj.c)


