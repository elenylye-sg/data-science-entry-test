class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    def __init__(self, make: str, model: str, year: int):
        """Initialize the car's core attributes."""
        self.make = make        # Manufacturer (e.g., Toyota)
        self.model = model      # Specific version (e.g., Corolla)
        self.year = year        # Manufacturing year
    def describe_car(self):
        print("Car:")
        print(f"  {self.make}")
        print(f"  {self.model}")
        print(f"  {self.year}")


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020
if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2020)
    car1.describe_car()
