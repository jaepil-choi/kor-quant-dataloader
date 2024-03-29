from abc import ABC, abstractmethod

import pandas as pd

class BaseDataReader(ABC):
    def __init__(self) -> None:
        pass

    @classmethod
    @abstractmethod
    def get_available_cols(cls) -> list:
        raise NotImplementedError

    @abstractmethod
    def read(
        self,
        data: str,
        start_date: str,
        end_date: str,
        download: bool
        ) -> pd.DataFrame:
        raise NotImplementedError
    
    @abstractmethod
    def _fetch_data_all(self):
        raise NotImplementedError
    
    @abstractmethod
    def _fetch_local_data(self) -> pd.DataFrame:
        raise NotImplementedError

    @abstractmethod
    def _get_available_local_dates(self) -> list:
        pass

    @abstractmethod
    def _filter_data(self) -> pd.DataFrame:
        raise NotImplementedError

    @abstractmethod
    def _show_catalog(self) -> pd.DataFrame:
        raise NotImplementedError

class BaseLocal:
    def __init__(self) -> None:
        pass

    def read_json(self) -> dict:
        pass

    def read_hdf(self) -> pd.DataFrame:
        pass

    def write_hdf(self) -> None:
        pass