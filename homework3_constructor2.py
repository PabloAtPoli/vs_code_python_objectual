
class Horse:
    def __init__(self, name, age, color = "white", rider = "John"):
        self.name = name
        self.age = age
        self.color = color
        self.rider = rider
      

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Color: {self.color}, Rider: {self.rider}"
        
    
horse = Horse(name = "Django", age=5, color="Brown", rider="Pablo")

print("Horse object:")
print(horse)

print("Horse dictionary:")
print(horse.__dict__)

      