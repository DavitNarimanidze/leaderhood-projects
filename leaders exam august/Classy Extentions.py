from preloaded import Animal

class Cat(Animal):
    def __init__(self , name ):
        self.name = name
        
    def speak(self):
        return f"{self.name} meows."
    
#მეორე 8 kyu 