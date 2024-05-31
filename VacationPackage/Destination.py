class Destination:
    def __init__(self):
        self.fav_destinations = {'Paris': 500, 'NYC': 600}
    
    def get_extra_cost(self, destination):
        return self.fav_destinations.get(destination, 0)
    
    def is_valid_destination(self, destination):
        return isinstance(destination, str)
