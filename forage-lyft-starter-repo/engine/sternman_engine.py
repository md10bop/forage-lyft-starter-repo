from engine.engine import Engine

class CapuletEngine(Engine):
    def __init__(self, warning_light_on):
        super().__init__()
        self.warning_light_on = warning_light_on

    def should_service(self):
        return self.warning_light_on