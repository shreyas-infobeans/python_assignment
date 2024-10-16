class Flight:
    def __init__(self,engine):
        self.engine = engine
    
    def startEngine(self):
        self.engine.start()

class AirBusEngine:
    def start(self):
        print("Starting Air Bus Engine")

class BoingEngine:
    def start(self):
        print("Start Boing ENgine")

ae = AirBusEngine()

f = Flight(ae)

f.startEngine()