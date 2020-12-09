import unittest
from models.country import Country

class TestCountry(unittest.TestCase):


    def setUp(self):
        self.country = Country("UAE")
    
    def test_country_has_name(self):
        self.assertEqual("UAE", self.country.name)

  # won't show up error or show up as test passed for countries