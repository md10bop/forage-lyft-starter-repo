import unittest
from datetime import date

from battery.nubbin import Nubbin
from battery.spindler import Spindler

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import Sternman
from engine.willoughby_engine import Willboughly



class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-09-12")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = Nubbin(current_date, last_service_date, 4)
        self.assertTrue(battery.should_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = Nubbin(current_date, last_service_date, 4)
        self.assertFalse(battery.should_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-09-12")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = Spindler(current_date, last_service_date, 2)
        self.assertTrue(battery.should_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = Spindler(current_date, last_service_date, 2)
        self.assertFalse(battery.should_service())

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.should_service())

    def test_needs_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.should_service())

class TestWillookjkEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = Willboughly(current_mileage, last_service_mileage)
        self.assertTrue(engine.should_service())

    def test_needs_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = Willboughly(current_mileage, last_service_mileage)
        self.assertFalse(engine.should_service())

class TestSternmanine(unittest.TestCase):
    def test_needs_service_true(self):
        waenign_light_on = True
        engine = Sternman(waenign_light_on)
        self.assertTrue(engine.should_service())

    def test_needs_service_true(self):
        waenign_light_on = False
        engine = Sternman(waenign_light_on)
        self.assertFalse(engine.should_service())