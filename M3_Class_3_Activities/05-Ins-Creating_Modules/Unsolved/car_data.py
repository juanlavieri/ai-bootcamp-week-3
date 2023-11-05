# Import the Car class from the car.py file.
from Car import Car
# Create an instance of the Car class.
car = Car("Toyota", "Camry", "Sedan", "V6", 2019, "Black")
# Get the current make using the getter methods.
print('Here are the details of the car.')
print(f"Make: {car.get_make()}")
print(f"Model: {car.get_model()}")
print(f"Body: {car.get_body()}")
print(f"Engine Type: {car.get_engine()}")
print(f"Year made: {car.get_year()}")
print(f"Color: {car.get_color()}")


# Prompt the user to change three parameters for the car.
new_make = input("What is the new make of the car? ")
new_model = input("What is the new model of the car? ")
new_body = input("What is the new body of the car? ")

# Use the setter methods to change the information
car.set_make(new_make)
car.set_model(new_model)
car.set_body(new_body)

# Print the new details about the car.
print('Here are the updated details of the car.')
print(f"Make: {car.get_make()}")
print(f"Model: {car.get_model()}")
print(f"Body: {car.get_body()}")
print(f"Engine Type: {car.get_engine()}")
print(f"Year made: {car.get_year()}")
print(f"Color: {car.get_color()}")
