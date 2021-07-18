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

        expected_release = """Rental record for Chango\n"""\
                           """ToyStory: 15\n"""\
                           """Amount owed is $15\n"""\
                           """You earned 2 frequent renter points"""
        self.assertEqual(self.customer.statements(), expected_release)


    def test_regular_movie(self):
        matrix = Movie("Matrix", Movie.REGULAR)
        rental = Rental(matrix, 1)
        self.customer.add_rental(rental)

        expected_regular = """Rental record for Chango\n"""\
                           """Matrix: 2\n"""\
                           """Amount owed is $2\n"""\
                           """You earned 1 frequent renter points"""
        self.assertEqual(self.customer.statements(), expected_regular)

    def test_children_movie(self):
        pets = Movie("Pets", Movie.CHILDRENS)
        rental = Rental(pets, 1)
        self.customer.add_rental(rental)

        expected_children = """Rental record for Chango\n"""\
                            """Pets: 1.5\n"""\
                            """Amount owed is $1.5\n"""\
                            """You earned 1 frequent renter points"""
        self.assertEqual(self.customer.statements(), children_regular)

class TestHtmlOutput(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Chango")

    def tearDown(self):
        self.customer.rentals.clear()

    def test_new_release(self):
        matrix = Movie("ToyStory", Movie.NEW_RELEASE)
        rental = Rental(matrix, 5)
        self.customer.add_rental(rental)

        expected_release = """<H1>Rental record for <EM>Chango</EM></H1><P>\n"""\
                           """ToyStory: 15\n"""\
                           """<P>Amount owed is <EM>$15</EM>\n"""\
                           """You earned 2 frequent renter points<P>"""
        self.assertEqual(self.customer.html_statements(), expected_release)


    def test_regular_movie(self):
        matrix = Movie("Matrix", Movie.REGULAR)
        rental = Rental(matrix, 1)
        self.customer.add_rental(rental)

        expected_regular = """<H1>Rental record for <EM>Chango</EM></H1><P>\n"""\
                            """Matrix: 2\n"""\
                            """<P>Amount owed is <EM>$2</EM>\n"""\
                            """You earned 1 frequent renter points<P>"""
        self.assertEqual(self.customer.html_statements(), expected_regular)

    def test_children_movie(self):
        pets = Movie("Pets", Movie.CHILDRENS)
        rental = Rental(pets, 1)
        self.customer.add_rental(rental)

        expected_children = """<H1>Rental record for <EM>Chango</EM></H1><P>\n"""\
                            """Pets: 1.5\n"""\
                            """<P>Amount owed is <EM>$1.5</EM>\n"""\
                            """You earned 1 frequent renter points<P>"""
        self.assertEqual(self.customer.html_statements(), expected_children)

