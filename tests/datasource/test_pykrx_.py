import pandas as pd

from kor_quant_dataloader.datasource.pykrx_ import (
    PykrxReader,
    PykrxOHLCV,
)

class TestPykrxReader:
    def test_read(self):
        pass
class TestPykrxOHLCV:
    def test_read(self):
        reader = PykrxOHLCV()
        df = reader.read(
            data=['종가'],
            start_date='2021-01-01',
            end_date='2021-01-05',
            download=False
            )

        assert isinstance(df, pd.DataFrame)
        
        df = reader.read(
            data='종가',
            start_date='2021-01-01',
            end_date='2021-01-05',
            download=False
            )

        assert isinstance(df, pd.DataFrame)