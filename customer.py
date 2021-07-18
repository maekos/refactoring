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

            this_amount = self.amount_for(rental)

            frequent_renter_points += 1
            if rental.get_movie().get_price_code() == Movie.NEW_RELEASE and rental.get_days_rented() > 1:
                frequent_renter_points += 1

            result += "{}: {}\n".format(rental.get_movie().get_title(), str(this_amount))
            total_amount += this_amount

        # Add footer lines
        result += "Amount owed is ${}\n".format(total_amount)
        result += "You earned {} frequent renter points".format(frequent_renter_points)
        return result

    def amount_for(self, rental):
        this_amount = 0
        code = rental.get_movie().get_price_code()
        if code == Movie.REGULAR:
            this_amount += 2
            if rental.get_days_rented() > 2:
                this_amount += (rental.get_days_rented() - 2) * 1.5
        if code == Movie.NEW_RELEASE:
            this_amount += rental.get_days_rented() * 3
        if code == Movie.CHILDRENS:
            this_amount += 1.5
            if rental.get_days_rented() > 3:
                this_amount += (rental.get_days_rented() - 3) * 1.5
        return this_amount
