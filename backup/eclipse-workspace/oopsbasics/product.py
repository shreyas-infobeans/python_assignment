class Product:
    def __init__(self):
        self.name = "iphone"
        self.description = "This is awesome"
        self.price = 40000
    
    def display(self):
        print(self.name)
        print(self.description)
p1 = Product()
p1.display()
'''print(p1.description)
print(p1.name)
print(p1.price)'''

class Course:
    
    def __init__(self,name,ratings):
        self.name = name
        self.ratings = ratings
    
    def average(self):
        numberOfRatings = len(self.ratings)
        average = sum(self.ratings)/numberOfRatings
        print(average)
        
c1 = Course("Java",[1,2,3])
#print(c1.name)
#print(c1.ratings)
#c1.average()
        