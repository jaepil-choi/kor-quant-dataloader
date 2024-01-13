import pandas as pd
import pytest

import kor_quant_dataloader as kqdl

class TestDateUtils:
    def test_get_daterange(self):
        assert kqdl.DateUtil.get_daterange(
            start_date='2021-12-25',
            end_date='2022-01-05',
            is_inclusive=True
            ) == [
                '2021-12-25',
                '2021-12-26',
                '2021-12-27',
                '2021-12-28',
                '2021-12-29',
                '2021-12-30',
                '2021-12-31',
                '2022-01-01',
                '2022-01-02',
                '2022-01-03',
                '2022-01-04',
                '2022-01-05'
                ]
    
    def test_intdate_to_strdate(self):
        assert kqdl.DateUtil.intdate_to_strdate(20211225) == '2021-12-25'
    
    def test_intdate_to_timestamp(self):
        assert kqdl.DateUtil.intdate_to_timestamp(20211225) == pd.Timestamp('2021-12-25 00:00:00')  
    
    def test_validate_date(self):
        assert kqdl.DateUtil.validate_date('2021-12-25') == None
        
        with pytest.raises(ValueError):
            kqdl.DateUtil.validate_date('2021-13-25')
    
    def test_add_strdt(self):
        assert kqdl.DateUtil.add_strdt('2021-12-25', 1) == '2021-12-26'
        assert kqdl.DateUtil.add_strdt('2021-12-25', -1) == '2021-12-24'

        