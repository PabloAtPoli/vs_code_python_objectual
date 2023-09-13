
class Horse:
    def __init__(self, name, age, color, rider):
        self.name = name
        self.age = age
        self.color = color
        self.rider = rider
      
    
    def print_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Color: ", self.color)
        print("Rider: ", self.rider)
        
    
horse = Horse(name = "Django", age=5, color="Brown", rider="Pablo")
horse.print_info()

    
