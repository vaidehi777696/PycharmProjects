from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyer=n
    @abstractmethod
    def start(self):
        pass