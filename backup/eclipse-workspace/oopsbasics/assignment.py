class Patient:
      
    def setId(self,i):
        self.__id = i
        
    def getId(self):
        return self.__id
    
    def setName(self,name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
    def setSsn(self,ssn):
        self.__ssn = ssn
        
    def getSsn(self):
        return self.__ssn
    
p1 = Patient()
p1.setId(3)
print(p1.getId())

p1.setName("shreyas")
print(p1.getName())

p1.setSsn(4455)
print(p1.getSsn())

