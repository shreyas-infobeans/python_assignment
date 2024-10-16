class Patient:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.clinical = []
    def addClinicalData(self,clinical):
        self.clinical.append(clinical)

class Clinical:
    def __init__(self,componentName, ComponentValue):
        self.componentName = componentName
        self.componentValue = ComponentValue
        
p1 = Patient("Shreyas",20)
c1 = Clinical('bp','80/100')
p1.addClinicalData(c1)
c2 = Clinical('heartrate',80)
p1.addClinicalData(c2)

for eachClinical in p1.clinical:
    print(eachClinical.componentName)
    print(eachClinical.componentValue)
