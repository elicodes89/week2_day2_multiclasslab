class Bus: 
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passenger = []

    def drive(self):
        return ("Brum brum")

    def passenger_count(self):
        return len(self.passenger)

    def pick_up(self, person):
        self.passenger.append(person)

    def drop_off(self, person):
        self.passenger.remove(person)

    def empty(self):
        self.passenger.clear()#this is a new method
    
    def pick_up_from_stop(self, bus_stop_to_pick_up_from):
        for passenger in bus_stop_to_pick_up_from.queue:
            self.passengers.append(passenger)
    

            


        
