import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City("Rome", False)

    def test_city_has_name(self):
        self.assertEqual("Rome", self.city.name)

    def test_destination_visited(self):
        self.assertEqual(False, self.city.visited)

    def test_can_mark_item_visited(self):
        self.city.mark_visited()
        self.assertEqual(True, self.city.visited)