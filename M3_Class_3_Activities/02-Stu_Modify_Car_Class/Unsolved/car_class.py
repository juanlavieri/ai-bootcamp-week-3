"""Creating a Car class with methods and instances"""

# Define the Car class
class Car:
    """Creating a Car class with 6 parameters and instances"""

    # Initialize the Car class with the following six parameters: "make", "model", "body", "engine", "year", and "color".
    def __init__(self, make, model, body, engine, year, color):
        # Create instance variables for each parameter.
        self.make = make
        self.model = model
        self.body = body
        self.engine = engine
        self.year = int(year)
        self.color = color

# Prompt the user to enter the information for the car for each parameter.
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
body = input("Enter the body type of the car: ")
engine = input("Enter the engine type of the car: ")
year = input("Enter the year of the car: ")
color = input("Enter the color of the car: ")

# Create an instance of the `Car` class and pass in the variables from the user.
car = Car(make, model, body, engine, year, color)

# Print the details of the car based on the user inputs.
print('Here is the information you entered for the car:')
print(f'Make: {car.make}')
print(f'Model: {car.model}')
print(f'Body: {car.body}')
print(f'Engine: {car.engine}')
print(f'Year: {car.year}')
print(f'Color: {car.color}')
