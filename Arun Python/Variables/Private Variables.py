class A:
    __a=10
    def __sample(self):
        print("Inside sample method of class A")
    def print_properties(self):
        print(self.__a)
        self.__sample()
obj=A()
obj.print_properties()
