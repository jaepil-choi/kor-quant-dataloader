import pykrx as krx

import pandas as pd

from functools import reduce

import time
from tqdm import tqdm

from kor_quant_dataloader.datasource.base import BaseDataReader
from kor_quant_dataloader.utils import DateUtil

class PykrxReader(BaseDataReader):
    @classmethod
    def get_available_cols(cls) -> list:
        available_cols = reduce(list.__add__, [child.get_available_cols() for child in cls.__subclasses__()])

        return available_cols

    def __init__(self) -> None:
        if not hasattr(self, 'available_cols'):
            raise AttributeError(f'{self.__class__.__name__}.available_cols should be defined.')
        
        # TODO: Check if the column names are already defined in other readers.
        # already_exist_cols = set(PykrxReader.get_available_cols()) & set(self.get_available_cols())
        # if already_exist_cols:
        #     raise AttributeError(f'Other readers already have column names {already_exist_cols}')
        # else:
        #     PykrxReader.available_cols += self.available_cols

        self.data = None
        self.start_date = None
        self.end_date = None
        self.download = None

        self.date_list = []
        self.holidays = []

    def read(
        self,
        data: str,
        start_date: str,
        end_date: str,
        download: bool,
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

        fetched = self._fetch_data_all(self.date_list)
        filtered = self._filter_data(fetched)

        return filtered

    def _fetch_data_one(
            self,
            date: str
            ) -> pd.DataFrame:
        pass

    def _melt_data_one(
            self,
            di_snapshot: pd.DataFrame,
            date: str
            ) -> pd.DataFrame:
        
        di_snapshot.reset_index(inplace=True)
        di_snapshot.rename(columns={'티커': 'ticker'}, inplace=True)
        di_snapshot.loc[:, 'date'] = date

        data_columns = [col for col in di_snapshot.columns if col not in ['ticker', 'date']]

        # Melt data for more robust data delivery. 
        di_snapshot = di_snapshot.melt(
            id_vars=['date', 'ticker'],
            value_vars=data_columns,
            var_name='data',
            value_name='value'
            )
        
        return di_snapshot

    def _fetch_data_all(
            self,
            date_list: list
            ) -> pd.DataFrame:
        
        di_snapshots = []
        for di in tqdm(date_list):
            melt = self._fetch_data_one(di)
            melt = self._melt_data_one(melt, di)
            di_snapshots.append(melt)
        
        df = pd.concat(di_snapshots, axis=0)

        return df

    def _fetch_local_data(
            self,
            date_list: list
            ) -> pd.DataFrame:
        pass

    def _get_available_local_dates(self) -> list:
        pass

    def _filter_data(self, df) -> pd.DataFrame:
        df = df[df['data'].isin(self.data)].copy()

        return df

    def _remove_holidays(self) -> pd.DataFrame:
        pass

    def _show_catalog(self) -> pd.DataFrame:
        pass

class PykrxOHLCV(PykrxReader):
    available_cols = [
            '시가',
            '고가',
            '저가',
            '종가',
            '거래량',
            '거래대금',
            '등락률',
        ]

    @classmethod
    def get_available_cols(cls) -> list:

        return cls.available_cols
    
    def __init__(self) -> None:
        super().__init__()

    def _fetch_data_one(
            self, 
            date: str,
            ) -> pd.DataFrame:
        di_snapshot = krx.stock.get_market_ohlcv_by_ticker(date, market='ALL')

        return di_snapshot

class PykrxMarketCap(PykrxReader):
    available_cols = [
        '시가총액',
        '거래량',
        # '거래대금', # OHLCV의 거래대금과 겹친다. 서로 다른 정보인가 같은 정보인가? 
        '상장주식수',
    ]

    @classmethod
    def get_available_cols(cls) -> list:

        return cls.available_cols
    
    def __init__(self) -> None:
        super().__init__()

    def _fetch_data_one(
            self, 
            date: str,
            ) -> pd.DataFrame:
        di_snapshot = krx.stock.get_market_cap_by_ticker(date, market='ALL')

        return di_snapshot

class PykrxFunda(PykrxReader):
    available_cols = [
        'BPS',
        'PBR',
        'PER',
        'EPS',
        'DIV',
        'DPS',
    ]

    @classmethod
    def get_available_cols(cls) -> list:

        return cls.available_cols
    
    def __init__(self) -> None:
        super().__init__()

    def _fetch_data_one(
            self, 
            date: str,
            ) -> pd.DataFrame:
        di_snapshot = krx.stock.get_market_fundamental(date, market='ALL')

        return di_snapshot