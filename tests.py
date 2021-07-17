import unittest
from customer import Customer
from movie import Movie
from rental import Rental


class TestRefactoring(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Chango")

    def tearDown(self):
        self.customer.rentals.clear()

    def test_new_release(self):
        matrix = Movie("ToyStory", Movie.NEW_RELEASE)
        rental = Rental(matrix, 5)
        self.customer.add_rental(rental)

        expected_release ="""Rental record for Chango
ToyStory: 15
Amount owed is $15
You earned 2 frequent renter points"""
        self.assertEqual(self.customer.statements(), expected_release)


    def test_regular_movie(self):
        matrix = Movie("Matrix", Movie.REGULAR)
        rental = Rental(matrix, 1)
        self.customer.add_rental(rental)

        expected_regular ="""Rental record for Chango
Matrix: 2
Amount owed is $2
You earned 1 frequent renter points"""
        self.assertEqual(self.customer.statements(), expected_regular)

    def test_children_movie(self):
        pets = Movie("Pets", Movie.CHILDRENS)
        rental = Rental(pets, 1)
        self.customer.add_rental(rental)

        expected_regular ="""Rental record for Chango
Pets: 1.5
Amount owed is $1.5
You earned 1 frequent renter points"""
        self.assertEqual(self.customer.statements(), expected_regular)
