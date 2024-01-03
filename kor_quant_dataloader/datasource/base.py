from abc import ABC, abstractmethod

class DataSourceInterface(ABC):
    """Abstract class that defines the interface for a data source.

    """    

    @abstractmethod
    def __repr__(self):
        pass

    