import unittest

from engine.engines import CapuletEngine, SternmanEngine, WilloughbyEngine

class TestCapuletEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        engine = CapuletEngine(60000, 20000)
        self.assertTrue(engine.needs_service())

    def test_engine_doesnt_needs_service(self):
        engine = CapuletEngine(60000, 50000)
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_engine_doesnt_needs_service(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        engine = WilloughbyEngine(100000, 10000)
        self.assertTrue(engine.needs_service())

    def test_engine_doesnt_needs_service(self):
        engine = WilloughbyEngine(20000, 10000)
        self.assertFalse(engine.needs_service())



if __name__ == '__main__':
    unittest.main()