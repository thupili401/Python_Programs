class car:
    def __init__(self,Brand,Price,Colour,Milage):
        self.Brand=Brand
        self.Price=Price
        self.Colour=Colour
        self.Milage=Milage
    def Hundai(self):
        print("My car is",self.Brand,"\nMy car price is :",self.Price,"\nMy car colour is :",self.Colour,"\nMy car milage is :",self.Milage)
    def Maruthi(self):
        print("My car is", self.Brand, "\nMy car price is :", self.Price, "\nMy car colour is :", self.Colour,"\nMy car milage is :",self.Milage)

    def Ford(self):
        print("My car is", self.Brand, "\nMy car price is :", self.Price, "\nMy car colour is :", self.Colour,"\nMy car milage is :", self.Milage)

obj=car("i10","3.75L","red","18")
obj2=car("I20","15L","PINK","20")
obj3=car("I30","20L","Black","10")
obj4=car("I40","1L","white","9")

obj2.Hundai()
print("................")
obj3.Maruthi()
print("................")
obj4.Ford()