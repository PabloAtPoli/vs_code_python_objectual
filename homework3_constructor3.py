class Horse:
    def __init__(self, name, color="White", age=0):
        self.name = name
        self.color = color
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Age:", self.age)

    def custom_print(self):
        print("Custom Print:")
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

# Create an object of the Horse class
horse = Horse(name="Spirit", color="Brown")

# Display the attributes using the display_info() method
horse.display_info()

# Call the custom_print() method
horse.custom_print()
