class car:

    wheels=4
    def data1(self,Brand,colour,milage,Price):

        self.Brand=Brand
        self.colour=colour
        self.milage=milage
        self.Price=Price
        print("My car is :", Brand , "\nMy car colour is :", colour, "\nMy car milage is :", milage, "\nMy car price is :",
              Price)
    def data2(self,Brand,colour,milage,Price):
        print("My car is :", Brand, "\nMy car colour is :", colour, "\nMy car milage is :", milage, "\nMy car price is :",
              Price)

obj=car()
obj.data1("i10","Red","18km","3.75L")
obj.data2("slavia","Black","13km","15L")