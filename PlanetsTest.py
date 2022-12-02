import unittest

from Planets import Planets
from assertpy import *

class PlanetsTest(unittest.TestCase):
    def setUp(self):
        self.temp = Planets()

    def testAgeOnMercury(self):
        assert_that(self.temp.get_age_on_planet("merkury", 10000000)).is_equal_to("1.32")

    def testAgeOnVenus(self):
        assert_that(self.temp.get_age_on_planet("wenus", 1000000000)).is_equal_to("51.51")

    def testIncorrectAgeOnMars(self):
        assert_that(self.temp.get_age_on_planet("mars", 1000000000)).is_not_equal_to("15.15")

    def testAgeIsNotNone(self):
        assert_that(self.temp.get_age_on_planet("jowisz", 100)).is_not_none()

    def testAgeIsCloseTo(self):
        assert_that(float(self.temp.get_age_on_planet("uran", 1000000000))).is_close_to(0, 0.5)

    def testRaisesExceptionOnWrongPlanet(self):
        assert_that(self.temp.get_age_on_planet).raises(Exception).when_called_with("pluton", 100000000)

    def testRaisesExceptionOnNonNumericAge(self):
        assert_that(self.temp.get_age_on_planet).raises(Exception).when_called_with("merkury", "test")

    def testIsAlwaysPositive(self):
        assert_that(float(self.temp.get_age_on_planet("merkury", 10000000000))).is_greater_than(0)

    def testAgeIsBetweenNumbers(self):
        assert_that(float(self.temp.get_age_on_planet("jowisz", 1000000000))).is_between(2.0, 3.0)

    def testOnMarsIsSmallerThanOnEarth(self):
        assert_that(float(self.temp.get_age_on_planet("mars", 1000000))).is_less_than(float(self.temp.get_age_on_planet("ziemia", 1000000)))
