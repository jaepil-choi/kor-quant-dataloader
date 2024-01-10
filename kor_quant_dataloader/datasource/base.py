from abc import ABC, abstractmethod

import pandas as pd

class BaseDataReader(ABC):
    def __init__(self) -> None:
        self.

    @abstractmethod
    def read(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def _fetch_data(self):
        pass
    
    @abstractmethod
    def _fetch_local_data(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def _transform_data(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def _show_catalog(self) -> pd.DataFrame:
        pass

    