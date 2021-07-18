from movie import Movie

class Rental:
    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented

    def get_days_rented(self):
        return self.days_rented

    def get_movie(self):
        return self.movie

    def get_charge(self):
        return self.movie.get_charge(self.days_rented)

    def get_frequent_renter_points(self):
        return self.movie.get_frequent_renter_points(self.days_rented)
