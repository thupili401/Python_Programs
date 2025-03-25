def args(*args):
    for i in args:
        print(i)
args(1,2,3)


def kwargs(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
kwargs(Name="sreekanth",place="lingampalli",work="EMbibe")