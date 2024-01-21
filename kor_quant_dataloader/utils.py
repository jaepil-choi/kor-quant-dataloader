import numpy as np
import pandas as pd

from collections import defaultdict

class DateUtil:
    @staticmethod
    def get_daterange(
        start_date: str,
        end_date: str,
        is_inclusive: bool = True
        ) -> list:
        DateUtil.validate_date(start_date)
        DateUtil.validate_date(end_date)

        if is_inclusive:
            end_date = DateUtil.add_strdt(end_date, 1)
        
        return pd.date_range(start_date, end_date).strftime('%Y-%m-%d').tolist()
        

    @staticmethod
    def intdate_to_strdate(
        intdate: int
        ) -> str:
        dt = str(intdate)
        strdt = f'{dt[:4]}-{dt[4:6]}-{dt[6:]}'
        
        DateUtil.validate_date(strdt)

        return strdt

    @staticmethod
    def strdt_to_intdate(
        strdt: str
        ) -> int:
        DateUtil.validate_date(strdt)

        return int(strdt.replace('-', ''))

    @staticmethod
    def intdate_to_timestamp(
        intdate: int
        ) -> pd.Timestamp:
        
        return pd.to_datetime(DateUtil.intdate_to_strdate(intdate))

    @staticmethod
    def validate_date(
        date: str
        ) -> bool:
        assert pd.to_datetime(date, format='%Y-%m-%d'), f'Invalid date format: {date}'
    
    @staticmethod
    def add_strdt(
        strdt: str,
        days: int,
        ) -> str:
        DateUtil.validate_date(strdt)

        return (pd.to_datetime(strdt) + pd.Timedelta(days=days)).strftime('%Y-%m-%d')
    
class CommonOps:
    @staticmethod
    def invert_dict(
        d: dict
        ) -> dict:
        return {v: k for k, v in d.items()}
    
    @staticmethod
    def invert_dict_of_lists(
        d: dict
        ) -> dict:
        return {v: k for k, v_list in d.items() for v in v_list}

    @staticmethod
    def invert_Nto1_dict(
        d: dict
        ) -> dict:
        dd = defaultdict(list)

        for k, v in d.items():
            dd[v].append(k)
        
        return dict(dd)

class PdOps:
    @staticmethod
    def molten_to_single(
        melt_df: pd.DataFrame,
        ) -> pd.DataFrame:
        assert melt_df['data'].unique().size == 1, 'Dataframe contains multiple data types.'

        single = melt_df.pivot(index='date', columns='ticker', values='value')
        single.sort_index(inplace=True)

        return single

    @staticmethod
    def molten_to_multi(
        melt_df: pd.DataFrame,
        ) -> pd.DataFrame:

        multi = melt_df.pivot_table(index=['date', 'ticker'], columns='data', values='value')
        multi.sort_index(inplace=True)

        return multi