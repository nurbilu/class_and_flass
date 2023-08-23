class Car:
    def __init__(self, make, model, year, color, fuel_type):
        self.make = make          # Make of the car (e.g., Toyota)
        self.model = model        # Model of the car (e.g., Camry)
        self.year = year          # Year the car was manufactured (e.g., 2023)
        self.color = color        # Color of the car (e.g., Red)
        self.fuel_type = fuel_type  # Fuel type of the car (e.g., Gasoline)
        self.speed = 0            # Current speed of the car (in mph)
        self.is_running = False   # Whether the car's engine is running or not

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.year} {self.make} {self.model}'s engine is now running.")
        else:print(f"{self.year} {self.make} {self.model}'s engine is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.speed = 0
            print(f"{self.year} {self.make} {self.model}'s engine is now off.")
        else:print(f"{self.year} {self.make} {self.model}'s engine is already off.")

    def accelerate(self, speed_increase):
        if self.is_running:
            self.speed += speed_increase
            print(f"{self.year} {self.make} {self.model} is now traveling at {self.speed} mph.")
        else:print(f"Cannot accelerate. {self.year} {self.make} {self.model}'s engine is off.")

    def brake(self, speed_decrease):
        if self.is_running:
            self.speed = max(0, self.speed - speed_decrease)
            print(f"{self.year} {self.make} {self.model} slowed down to {self.speed} mph.")
        else:print(f"Cannot brake. {self.year} {self.make} {self.model}'s engine is off.")

    def honk(self):
        print(f"{self.year} {self.make} {self.model} says 'Honk! Honk!'")

    def get_speed(self):
        return self.speed

# Example usage:
my_car = Car("Toyota", "Camry", 2023, "Red", "Gasoline")
my_car.start()
my_car.accelerate(30)
my_car.brake(10)
my_car.honk()
my_car.stop()
