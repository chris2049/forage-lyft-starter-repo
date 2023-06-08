from car import Car
from engines import CapuletEngine, SternmanEngine, WilloughbyEngine


class CarFactory():
    def  create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = ''

        return Car(engine, battery)

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = ''

        return Car(engine, battery)
    
    def create_glissade(last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = ''
        
        return Car(engine, battery)
    
    def create_rorschach(last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = ''
        
        return Car(engine, battery)
    
    def create_pallindrome(last_service_date, warning_light_is_on):
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        battery = ''

        return Car(engine, battery)