from datetime import date
class Eventmy:
    def __init__(self,starttime,endtime,venue):
        self.starttime = starttime
        self.endtime = endtime
        self.venue = venue
    def show(self):
        print(f"Event at {self.venue.name} on {self.starttime} to {self.endtime} address is {self.venue.address.street} {self.venue.address.city} {self.venue.address.state} {self.venue.address.country}")

class Venue:
    def __init__(self,name,address):
        self.name = name
        self.address = address
class Address:
    def __init__(self,street,city,country, state):
        self.street = street
        self.city = city
        self.country = country
        self.state = state
    

add = Address("mg rd","pune","In","MH")
ven = Venue("Maine",add)
eve = Eventmy(date(2024,7,12),date(2024,7,13),ven)
eve.show()
        