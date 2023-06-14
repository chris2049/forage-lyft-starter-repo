from car import Car
from engine.engines import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery.batteries import NubbinBattery, SpindlerBattery
from tire.tires import OctoprimeTire, CarriganTire

class CarFactory():
    @staticmethod
    def  create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = CapuletEngine( current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
    

        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)

        return Car(engine, battery)
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        
        return Car(engine, battery)
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        
        return Car(engine, battery)
    
    @staticmethod
    def create_pallindrome(current_date, last_service_date, warning_light_is_on, tire_array):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)

        return Car(engine, battery)