from engine.engine import Engine

class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        super().__init__()
        
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def is_service_due(self):
        mileage_difference = self.current_mileage - self.last_service_mileage
        return mileage_difference > 60000

    def should_service(self):
        return self.is_service_due()