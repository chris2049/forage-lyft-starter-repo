from abc import ABC

from serviceable import Serviceable


class Car(Serviceable, ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        if self.battery.needs_service() or self.engine.needs_service():
            return True
        else:
            return False

