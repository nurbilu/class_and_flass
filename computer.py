class Computer:
    # Constructor to initialize a Computer object.
    def __init__(self, brand, model, cpu, ram, storage):
        self.brand = brand
        self.model = model
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.powered_on = False

    # Method to power on the computer.
    def power_on(self):
        if not self.powered_on:
            print(f"{self.brand} {self.model} is powering on...")
            self.powered_on = True
        else:
            print("Computer is already powered on.")

    # Method to power off the computer.
    def power_off(self):
        if self.powered_on:
            print(f"{self.brand} {self.model} is powering off...")
            self.powered_on = False
        else:
            print("Computer is already powered off.")

    # Method to display information about the computer.
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"CPU: {self.cpu}")
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB")
        print("Status: Powered on" if self.powered_on else "Status: Powered off")

# Example usage:
if __name__ == "__main__":
    my_computer = Computer("Dell", "XPS 13", "Intel Core i7", 16, 512)
    my_computer.display_info()
    my_computer.power_on()
    my_computer.power_off()
