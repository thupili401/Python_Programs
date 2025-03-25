from abc import ABC, abstractmethod


class A(ABC):
    #Abstraction method
    @abstractmethod
    def  method_one(self):
        pass

    # Abstraction method
    @abstractmethod
    def method_two(self):
        pass

    #  Non Abstraction method
    def method_three(self):
        print("Inside method three")
class B(A):
    def method_one(self):
        print("inside method one")
    def method_two(self):
        print("inside method two")
obj =B()
obj.method_one()
obj.method_two()
obj.method_three()


