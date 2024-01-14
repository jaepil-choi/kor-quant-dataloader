from pandas.core.api import DataFrame as DataFrame
import pykrx as krx

import pandas as pd

import time
from tqdm import tqdm

from kor_quant_dataloader.datasource.base import BaseDataReader
from kor_quant_dataloader.utils import DateUtil

class PykrxReader(BaseDataReader):
    def __init__(self) -> None:
        self.data = None
        self.start_date = None
        self.end_date = None
        self.download = None

        self.date_list = []

    def read(
        self,
        data: str,
        start_date: str,
        end_date: str,
        download: bool
        ) -> pd.DataFrame:

        self.data = data
        self.start_date = start_date
        self.end_date = end_date
        self.download = download

        self.date_list = DateUtil.get_daterange(
            self.start_date,
            self.end_date,
            is_inclusive=True
            )

        fetched = self._fetch_data_all()
        processed = self._preprocess_data(fetched)

        return processed

    def _fetch_data_one(
            self,
            date: str
            ) -> pd.DataFrame:
        pass

    def _fetch_data_all(
            self,
            date_list: list
            ) -> pd.DataFrame:
        
        di_snapshots = []
        for di in tqdm(date_list):
            di_snapshots.append(self._fetch_data_one(di))
        
        df = pd.concat(di_snapshots, axis=0)

        return df

    def _fetch_local_data(
            self,
            date_list: list
            ) -> pd.DataFrame:
        pass

    def _get_available_local_dates(self) -> list:
        pass

    def _preprocess_data(self) -> pd.DataFrame:
        pass

    def _remove_holidays(self) -> DataFrame:
        pass

    def _show_catalog(self) -> pd.DataFrame:
        pass

    



