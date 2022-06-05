from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, starting_top_speed=100):
        super().__init__(starting_top_speed)
        self.passengers = []

    def add_group(self, passengers):
        self.passengers.extend(passengers)

bus1 = Bus(100)
bus1.add_group(['Max', 'Manuel', 'Anna'])
bus1.add_group(['Gavin'])
print(bus1)
print(bus1.__dict__)
bus1.add_warning('test')
print(bus1)