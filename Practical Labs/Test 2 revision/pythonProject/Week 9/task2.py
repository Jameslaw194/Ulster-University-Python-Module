class House:
    count = 0

    def __init__(self, address, floors, rooms, heating):
        self.address = address
        self.floors = floors
        self.rooms = rooms
        self.heating = heating
        House.count += 1

    def __str__(self):
        return f"House at {self.address}: {self.floors} floors, {self.rooms} rooms, Heating type: {self.heating}"

    @classmethod
    def noOfHouses(cls):
        return cls.count

#house1 = House("123 Main St", 2, 3, "Gas")
#house2 = House("456 Elm Ave", 3, 4, "Electric")

#print(house1)
#print(house2)

#print(f"Total houses created: {House.noOfHouses()}")
