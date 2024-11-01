class Car:
    "BMW"
class Battery:
    125 

    def __init__(self, battery_size= 125):
        self.battery_size = battery_size
        print(f"This car has a {battery_size}-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 125:
         range = 469
        elif self.battery_size == 175:
         range = 703       
        print(f"This car can go about {range} miles on a full charge.")