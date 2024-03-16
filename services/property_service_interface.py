from abc import ABC, abstractmethod

class PropertyServiceInterface(ABC):
    @abstractmethod
    def add_property(self, id):
        pass

    @abstractmethod
    def mark_sold(self, property_id):
        pass
