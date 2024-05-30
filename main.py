class Destination:
    def __init__(self):
        self.fav_destinations = {'Paris': 500, 'NYC': 600}
    
    def get_extra_cost(self, destination):
        return self.fav_destinations.get(destination, 0)
    
    def is_valid_destination(self, destination):
        return isinstance(destination, str)

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

class TravelDuration:
    def __init__(self, duration):
        self.duration = duration

    def is_valid_duration(self):
        return isinstance(self.duration, int) and self.duration > 0

    def get_fee(self):
        return 200 if self.duration < 7 else 0

    def get_promo_discount(self):
        return 200 if self.duration > 30 else 0


class VacationPackage:
    base_cost = 1000

    def __init__(self, destination, num_passengers, duration):
        self.destination = Destination()
        self.passenger = Passenger(num_passengers)
        self.travel_duration = TravelDuration(duration)
        self.destination_name = destination

    def calculate_total_cost(self):
        if not self.destination.is_valid_destination(self.destination_name) or \
           not self.passenger.is_valid_number() or \
           not self.travel_duration.is_valid_duration():
            return -1
        total_cost = self.base_cost
        total_cost += self.destination.get_extra_cost(self.destination_name)
        total_cost += self.travel_duration.get_fee()
        total_cost -= self.travel_duration.get_promo_discount()
        total_cost -= self.passenger.get_promo_policy()

        discount = self.passenger.get_discount()
        total_cost -= total_cost * discount

        return max(int(total_cost), 0)

def main():
    destination = "Paris"
    num_passengers = 2
    duration = 10

    vacation = VacationPackage(destination, num_passengers, duration)
    total_cost = vacation.calculate_total_cost()

    if total_cost == -1:
        print("Invalid input.")
    elif num_passengers > 80:
        print("The vacation package is not available for groups of more than 80 people.")
    else:
        print(f"The total cost of the vacation package is: ${total_cost}")


if __name__ == "__main__":
    main()