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
        total_amount = 0
        frequent_renter_points = 0
        result = "Rental record for {}\n".format(self.name)
        for rental in self.rentals:
            frequent_renter_points += rental.get_frequent_renter_points()
            result += "{}: {}\n".format(rental.get_movie().get_title(), str(rental.get_charge()))
            total_amount += rental.get_charge()

        # Add footer lines
        result += "Amount owed is ${}\n".format(total_amount)
        result += "You earned {} frequent renter points".format(frequent_renter_points)
        return result

