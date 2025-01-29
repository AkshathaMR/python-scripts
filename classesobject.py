class example:
    def __init__(self, str1, str2, str3):
        self.str1= str1
        self.str2= str2
        self.str3= str3
        self.str4= "Learn"
        self.str5= "Devops"
    
    def print_value(self):
        print(self.str1, self.str2, self.str3, self.str4, self.str5)

    def print_values(self):
        print(self.str2)
example1 = example("Hi","Akshatha","welcome to ")
example1.print_value()
example1.print_values()
