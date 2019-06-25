#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""A class that models cars."""

class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):  ## TWO underscore 
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
# class Car():
#     """A class to model cars."""
    
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        

        
#     def get_descriptive_name(self): # no need for make etc.
#         """Return a well formated name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
    
#     def read_odometer(self):
#         """Print a statement reading a car's mileage."""
#         print("The car has " + str(self.odometer_reading) + " on it.")
        
#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to a given value.
#         Reject if tries to roll back the odometer reading.
#         """
#         if mileage > self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("Odometer cannot be rolled back.")
            
#     def increment_odometer(self, miles):
#         """Add miles to odometer."""
# #         self.odometer_reading = self.odometer_reading + miles
#         self.odometer_reading += miles
        
class Battery():
    """A class to model a battery for an electronic car."""

    def __init__(self, battery_size=60): 
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        # self.battery_size = 60 ???

    def describe_battery(self):
        """Print a statement about the battery size."""
        print("This car has a battery of " + str(self.battery_size) + ".")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 200
        elif self.battery_size == 80:
            range = 250
            
        message = "This car can go "  + str(range) + " on full charge."
        print(message)
        
class Electriccar(Car):
    """Models aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
# class ElectricCar(Car):
#     """Models aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()

