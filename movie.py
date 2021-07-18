
class Movie:
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        self.title = title
        self.price_code = price_code

    def get_charge(self, days_rented):
        result = 0
        code = self.get_price_code()
        if code == self.REGULAR:
            result += 2
            if days_rented > 2:
                result += (days_rented - 2) * 1.5
        if code == self.NEW_RELEASE:
            result += days_rented * 3
        if code == self.CHILDRENS:
            result += 1.5
            if days_rented > 3:
                result += (days_rented - 3) * 1.5
        return result

    def get_price_code(self):
        return self.price_code

    def set_price_code(self, value):
        self.price_code = value

    def get_title(self):
        return self.title

    def get_frequent_renter_points(self, days_rented):
        if self.get_price_code() == self.NEW_RELEASE and days_rented > 1:
            return 2
        return 1
