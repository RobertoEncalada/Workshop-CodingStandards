class Passenger:
    def __init__(self, num_passengers):
        self.num_passengers = num_passengers
    
    def is_valid_number(self):
        return isinstance(self.num_passengers, int) and self.num_passengers > 0

    def get_discount(self):
        if 4 < self.num_passengers < 10:
            return 0.1
        elif self.num_passengers >= 10:
            return 0.2
        else:
            return 0.0
        
    def get_promo_policy(self):
        return 200 if self.num_passengers == 2 else 0