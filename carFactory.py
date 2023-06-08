from car import Car
from engine.engines import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery.batteries import NubbinBattery, SpindlerBattery

class CarFactory():
    def  create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine( current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)

        return Car(engine, battery)

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)

        return Car(engine, battery)
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        
        return Car(engine, battery)
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        
        return Car(engine, battery)
    
    def create_pallindrome(current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)

        return Car(engine, battery)