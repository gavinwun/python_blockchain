from vehicle import Vehicle

class Car(Vehicle):
    # top_speed = 100
    # warnings = []

    def brag(self):
        print('Look how cool my car is!')

myCar = Car()
# myCar.top_speed = 20
myCar.add_warning('New warning')
print(myCar.__dict__)
print(myCar)
myCar.drive()


myCar2 = Car(300)
myCar2.brag()

print(myCar.get_warnings())