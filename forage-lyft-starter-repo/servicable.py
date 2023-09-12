from abc import ABC, abstractmethod


class Servicable(ABC):
    @abstractmethod
    def should_service(self):
        pass
