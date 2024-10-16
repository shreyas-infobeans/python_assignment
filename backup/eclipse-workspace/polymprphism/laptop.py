from abc import abstractmethod,ABC
class TouchScreenLaptop(ABC):
    
    @abstractmethod
    def scroll(self):
        pass
    
    @abstractmethod    
    def click(self):
        pass
         
class HP(TouchScreenLaptop):
    def scroll(self):
        print("Scroll HP")

class Dell(TouchScreenLaptop): 
    def scroll(self):
        print("Scroll Dell")
        
class HPNotebook(HP): 
    def click(self):
        print("Scroll hpnotebook")

hp = HPNotebook()
hp.click()  
hp.scroll()        
        