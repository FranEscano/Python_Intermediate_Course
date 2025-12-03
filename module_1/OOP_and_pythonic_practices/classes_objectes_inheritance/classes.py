class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along..")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle('BYD', 'F3')

# print("My car is a", my_car.make, my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Toyota', 'Corolla')
your_car.get_make_model()
your_car.moves()

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies along..")

    def get_faa_id(self):
        print(f"My faa id is {self.faa_id}.")

class Truck(Vehicle):
    def __init__(self, make, model, bed_size):
        super().__init__(make, model)
        self.bed_size = bed_size

    def moves(self):
        print("Rumbles along..")

    def get_bed_size(self):
        print(f"My bed size is {self.bed_size} feet.")

class GolfCart(Vehicle):
    pass

cesnna = Airplane('Cessna', 'Skyhawk', '12345')
mack = Truck('Mack', 'Pinnacle', 2)
golfwagon = GolfCart('Yamaha', 'GC100')

cesnna.get_make_model()
cesnna.moves()
cesnna.get_faa_id()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print('\n\n')

for v in (my_car, your_car, cesnna, mack, golfwagon):
    v.get_make_model()
    v.moves()