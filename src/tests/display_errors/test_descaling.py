# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestDescaling(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)
        # Given I handle coffee grounds
        self.actionwords.i_handle_coffee_grounds()
        # And I handle water tank
        self.actionwords.i_handle_water_tank()
        # And I handle beans
        self.actionwords.i_handle_beans()
        raise NotImplementedError

    def test_descaling_is_needed_after_500_coffees(self):
        # TODO: Implement action: "Given the coffee machine is started"
        # TODO: Implement action: "When I take = 500 coffees"
        # TODO: Implement action: "Then a notification about descaling is displayed"
        raise NotImplementedError
