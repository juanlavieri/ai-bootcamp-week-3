"""Creating a Car class with parameters and instances"""

# Define the Car class
class Car:
    """Creating a Car class with parameters"""
    
    # Define the __init__ method with parameters for make, model, and year
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Create an instance of the Car class using the user's input
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
year = input("Enter the year of the car: ")
car = Car(make, model, year)

# Print the details of the car
print(f"Car details: {car.make} {car.model} {car.year}")
