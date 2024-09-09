 # Define the Vehicle class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.running = False  # Default value for running

    def start(self):
        self.running = True
        print("Starting up!")

    def stop(self):
        self.running = False
        print("Turning off.")

    def __str__(self):
        return f"The vehicle is a {self.make} {self.model}."

# Instantiate a Vehicle object
car = Vehicle("Toyota", "RAV4")

# Print the vehicle's information
print(car)  # prints: The vehicle is a Toyota RAV4.

# Print the current running status
print(car.running)  # prints: False

# Start the vehicle
car.start()  # prints: Starting up!

# Print the updated running status
print(car.running)  # prints: True

# Stop the vehicle
car.stop()  # prints: Turning off.

# Print the updated running status again
print(car.running)  # prints: False