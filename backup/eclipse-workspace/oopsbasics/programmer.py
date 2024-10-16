class Programmer:
    def setName(self,n):
        self.name = n
    def getName(self):
        return self.name
    
    def setSalary(self,s):
        self.salary = s
        
    def getSalary(self):
        return self.salary
    
    def setTech(self,t):
        self.tech = t
        
    def getTech(self): 
        return self.tech   
    
p1 = Programmer()
p1.setName("Shreyas")
p1.setSalary(3000000)
p1.setTech("python")

print(p1.getName())
print(p1.getSalary())
print(p1.getTech())



