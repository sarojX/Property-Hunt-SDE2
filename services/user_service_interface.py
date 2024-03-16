from abc import ABC, abstractmethod

class UserServiceInterface(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def list_property(self, property):
        pass

    @abstractmethod
    def view_listed_property(self):
        pass

    @abstractmethod
    def shortlist_property(self, property_id):
        pass

    @abstractmethod
    def view_shortlisted_properties(self):
        pass
