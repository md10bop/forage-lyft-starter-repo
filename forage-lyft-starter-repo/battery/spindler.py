from datetime import datetime, timedelta

from battery.battery import Battery

class Spindler(Battery):
    def __init__(self, last_service, current_time, time_between_service):
        self.current_time = current_time
        self.last_service = last_service
        self.time_between_service = time_between_service

    def should_service(self):
        time_since_last_service = self.current_time - self.last_service

        service_time = timedelta(days=365 * self.time_between_service)

        return time_since_last_service >= service_time


