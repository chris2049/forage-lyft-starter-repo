import unittest

from tire.tires import CarriganTire, OctoprimeTire

class TestCarriganTire(unittest.TestCase):
    def test_CarriganTire_one_needs_service(self):
        tire_array = [.9,.0,.1,.2]
        tire = CarriganTire(tire_array)
        self.assertTrue(tire.needs_service())

    
    def test_CarriganTire_two_needs_service(self):
        tire_array = [.2,.9,.1,.2]
        tire = CarriganTire(tire_array)
        self.assertTrue(tire.needs_service())
        
    
    def test_CarriganTire_three_needs_service(self):
        tire_array = [.1,.5,.9,.2]
        tire = CarriganTire(tire_array)
        self.assertTrue(tire.needs_service())


    def test_CarriganTire_all_needs_service(self):
        tire_array = [.1,.4,.5,.9]
        tire = CarriganTire(tire_array)
        self.assertTrue(tire.needs_service())
                
    def test_CarriganTire_doesnt_needs_service(self):
        tire_array = [.1,.2,.3,.4]
        tire = CarriganTire(tire_array)
        self.assertFalse(tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_octoprimeTire_needs_service_gr3(self):
        tire_array = [1,2,3,4]
        tire = OctoprimeTire(tire_array)
        self.assertTrue(tire.needs_service())

    def test_octoprimeTire_needs_service_eq3(self):
        tire_array = [1,1,1,0]
        tire = OctoprimeTire(tire_array)
        self.assertTrue(tire.needs_service())

    def test_octoprimeTire_doesnt_needs_service(self):
        tire_array = [0,0,1,1]
        tire = OctoprimeTire(tire_array)
        self.assertFalse(tire.needs_service())

        

    