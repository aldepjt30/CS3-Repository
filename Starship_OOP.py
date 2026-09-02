class StarshipCargo:
    def __init__(self, baseweight=50000, cargo_weight=0, final_fuel=0):
        self.baseweight = baseweight
        self.cargo_weight = cargo_weight
        self.final_fuel = final_fuel

    def cargo_load(self):
        cargo = input("Enter cargo type (satellite, rover, supplies): ")
        if cargo == "satellite":
            self.cargo_weight += 10000
        elif cargo == "rover":
            self.cargo_weight += 5000
        elif cargo == "supplies":
            self.cargo_weight += 2000
        else:
            print("This cargo is invalid.")

    def calculate_fuel(self):
        total_weight = self.cargo_weight + self.baseweight
        self.final_fuel = total_weight * 3
        return self.final_fuel

starship = Starship(50000, 0, 0)
starship.cargo_load()

print(starship.calculate_fuel())