# Create a class, Cat, create a subclass of it, Tiger. How does it behave differently?

class Cat:
    max_speed = 50 # KM/HR
    max_calories = 500
    
    def __init__(self, size, weight):
        self.size = size
        self.weight = weight
        self.ate = 0
    
    def run(self, distance): # distance, in kilometers 
        time = (distance * self.max_speed) / 3600
        return f"{time:.1} hours"
    
    def eat(self, amount): # Calories
        self.ate += amount
        if amount > self.max_calories:
           raise ValueError("Can't eat anymore")
    
    def digest(self):
        self.ate = 0

class Tiger(Cat):
    max_speed = 65 # Km/Hr
    max_calories = 9000

    def __init__(self, size, weight, prey): # Cm, Kg
        super().__init__(size,weight)
        self.prey = prey
    
    def eat(self, amount): 
        super().eat(amount)
        return f"He has eaten a {self.prey}"
    
