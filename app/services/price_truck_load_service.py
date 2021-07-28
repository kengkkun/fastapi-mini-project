import random


class PriceTruckLoad:
    def __init__(self, variable_distance, round_trip_discount):
        self.fixed_cost = 1.5
        self.variable_distance = variable_distance
        self.round_trip_discount = round_trip_discount
        self.additional_stop = random.randint(1, 10)
        self.additional_staff = random.random() * 10

    def get_document(self):
        return_document = ((self.variable_distance / self.fixed_cost * self.round_trip_discount) * self.additional_stop) / self.additional_staff
        return return_document


