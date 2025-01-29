class Person:  
    def __init__(self, name, age,place):  
        self.name = name    
        self.age = age      
        self.place = place
    def greet(self):  
        print("Hi, I'am", {self.name} )
        print("My age is", {self.age} )
        print("Place is",{self.place})  
  
# Create a new instance of the Person class and assign it to the variable person1  
person1 = Person("Akshatha", 30,"Bangalore")  
person1.greet()
