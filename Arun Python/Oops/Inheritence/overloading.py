class a:
    def hi(self,name=None):
        if name is not None:
            print("Hello",name)
        else:
            print("Hello")
obj=a()
obj.hi("sreekanth")
obj.hi()