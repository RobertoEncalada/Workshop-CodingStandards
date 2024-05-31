from VacationPackage.Destination import Destination
from VacationPackage.Passenger import Passenger
from VacationPackage.TravelDuration import TravelDuration


class Vacation:
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

        return int(total_cost)