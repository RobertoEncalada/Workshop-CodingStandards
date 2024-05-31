class TravelDuration:
    def __init__(self, duration):
        self.duration = duration

    def is_valid_duration(self):
        return isinstance(self.duration, int) and self.duration > 0

    def get_fee(self):
        return 200 if self.duration < 7 else 0

    def get_promo_discount(self):
        return 200 if self.duration > 30 else 0