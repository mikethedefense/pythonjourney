class Plane:
    fuel_add=1000
    def __init__(self,name,passengers,manufacture,speed,fuel):
        self.name=name
        self.passengers=passengers
        self.manufacture=manufacture
        self.speed=speed
        self.fuel=fuel
    def add_fuel(self):
        self.fuel=int(self.fuel + self.fuel_add)
        

aircraft_1=Plane('B737-100',160,'Boeing',800,100000)


print(aircraft_1.fuel)
aircraft_1.add_fuel()
print(aircraft_1.fuel)
print(aircraft_1.name)
#Try a new instance or call different attributes on this instance
