import pandas as pd
import kor_quant_dataloader as kqdl

def test_show_catalog():
    assert isinstance(kqdl.show_catalog(), pd.DataFrame)

class TestDataLoader:
    def test_get_data(self):
        pykrx_loader = kqdl.DataLoader(
            source='pykrx',
            start_date='2021-01-01',
            end_date='2021-01-05',
            universe=['005930'],
            remove_holidays=True,
            )

        df = pykrx_loader.get_data(
            data=['종가'], 
            download=False,
            )
        
        assert isinstance(df, pd.DataFrame)