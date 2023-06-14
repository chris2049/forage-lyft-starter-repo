import unittest
from datetime import datetime

from battery.batteries import NubbinBattery, SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
       
        battery = NubbinBattery(today, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_battery_doesnt_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = NubbinBattery(today, last_service_date)

        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_date = last_service_date.replace(day=last_service_date.day - 1)
        battery = SpindlerBattery(today, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_battery_doesnt_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = SpindlerBattery(today, last_service_date)

        self.assertFalse(battery.needs_service())

        
