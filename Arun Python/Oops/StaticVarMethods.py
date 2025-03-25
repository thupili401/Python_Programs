class car:
    Wheels=4
    def __init__(self,Brand,Price,Colour,Milage,Modal):
        self.Brand=Brand
        self.Price=Price
        self.Colour=Colour
        self.Milage=Milage
        self.Modal=Modal
    def strart_car(self):
        print("My Car Brand is :",self.Brand , "Has Started :",self.Modal)
    @staticmethod
    def print_car_wheels():
        print(car.Wheels)

svdi=car("Maruthi","10L","White","24","Dezire")
print(svdi.Brand)
print(svdi.Milage)
print(svdi.Colour)
print(svdi.Wheels)
svdi.strart_car()
car.print_car_wheels()