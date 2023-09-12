from servicable import Servicable


class Car(Servicable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def should_service(self):
        return self.engine.should_service() or self.battery.should_service()