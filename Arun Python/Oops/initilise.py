class car:
    def initilizing_values(self,Brand,Price,Colour,Milage):
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

obj=car()
obj.initilizing_values("i10","3.75L","red","18")
obj2=car()
obj2.initilizing_values("I20","15L","PINK","20")
obj3=car()
obj3.initilizing_values("I30","20L","Black","10")
obj4=car()
obj4.initilizing_values("I40","1L","white","9")

obj2.Hundai()
print("................")
obj3.Maruthi()
print("................")
obj4.Ford()