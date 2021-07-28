class PriceItem:

    def __init__(self, sum_whd, weight, volumn):
        self.sum_whd = sum_whd
        self.weight = weight
        self.volumn = volumn

    def get_price(self):
        return self.sum_whd + self.volumn + self.weight



