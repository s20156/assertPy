import re
import unittest

from Worker import ProductionWorker
from assertpy import *

class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.temp = ProductionWorker("lastname", "firstname", "email@example.com", 2, 25.5)

    def testLastnameGetter(self):
        assert_that(self.temp.get_lastname()).is_equal_to("lastname")

    def testLastnameSetter(self):
        self.temp.set_lastname("Mayer")
        assert_that(self.temp.get_lastname()).is_equal_to("Mayer")

    def testLastnameSetsToNew(self):
        self.temp.set_lastname("Mayer")
        assert_that(self.temp.get_lastname()).is_not_equal_to("lsatname")

    def testFirstnameNotEmpty(self):
        assert_that(self.temp.get_firstname()).is_not_none()

    def testEmailMatchRegexp(self):
        regexp = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        assert_that(self.temp.get_email()).matches(regexp)

    def testHourlyWageCloseTo(self):
        assert_that(self.temp.get_pay_hour()).is_close_to(25, 0.5)

    def testHourlyWageNotNull(self):
        assert_that(self.temp.get_pay_hour()).is_not_none()

    def testChangeNumberBetween1and2(self):
        assert_that(self.temp.get_change_number()).is_between(1, 2)

    def testRaisesException(self):
        assert_that(self.temp.set_change_number).raises(Exception).when_called_with(5)

    def testRaiseExceptionOnAddingStringToHourlyPay(self):
        assert_that(self.temp.set_pay_hour).raises(Exception).when_called_with("test")