# Parent class is created
class Vehicle:
    def __init__(self, type, company, name): # initializes values everytime when child class are newly derived
        self.type = type
        self.company = company
        self.name = name


# the child classes are created which utilizes parent class attributes
class Bike(Vehicle):
    def description(self):
        return f'{self.type} is {self.company} {self.name}'
        
class FourWheeler(Vehicle):
    def description(self):
        return f'{self.type} is {self.company} {self.name}'

class Truck(Vehicle):
    def description(self):
        return f'{self.type} is {self.company} and name is {self.name}'

if __name__ == '__main__':

    # here specific values are given which to child classes on the basis of parent class attributes
    # but these values are hard-coded.
    # We must print results according to user input
    Unicorn = Bike('Bike','Honda', 'Unicorn')
    Ciaz = FourWheeler('Car', 'Maruti', 'Ciaz')
    Forge = Truck('Truck','Bharat Benz','Forge')

    # function from child class is called here
    print(Unicorn.description())
    print(Ciaz.description())
    print(Forge.description())
    
    # for car in (blue_car, red_car):
    #     print(f"The {car.color} car has {car.mileage:,} miles")
