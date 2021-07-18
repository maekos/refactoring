from movie import Movie

class Customer:
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)

    def get_name(self):
        return self.name

    def statements(self):
        frequent_renter_points = 0
        result = "Rental record for {}\n".format(self.name)
        for rental in self.rentals:
            result += "{}: {}\n".format(rental.get_movie().get_title(), str(rental.get_charge()))

        # Add footer lines
        result += "Amount owed is ${}\n".format(self.get_total_charge())
        result += "You earned {} frequent renter points".format(self.get_total_frequent_renter_points())
        return result

    def get_total_charge(self):
        result = 0
        for rental in self.rentals:
            result += rental.get_charge()
        return result

    def get_total_frequent_renter_points(self):
        result = 0
        for rental in self.rentals:
            result += rental.get_frequent_renter_points()
        return result
