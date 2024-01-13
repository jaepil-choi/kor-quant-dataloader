import numpy as np
import pandas as pd

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
    
