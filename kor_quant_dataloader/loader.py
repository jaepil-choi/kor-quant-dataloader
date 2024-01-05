import numpy as np
import pandas as pd
from typing import Union, List

def show_catalog() -> pd.DataFrame:
    """
    Displays the collection of available data in the catalog.

    This method should be the initial call to view the available datasets. Each dataset 
    includes information such as the data source (external library), data name, and any 
    applicable optional parameters (e.g., fill='ffill'). The catalog is aggregated 
    automatically from each data source object, eliminating the need for manual updates.

    """    
    pass

class DataLoader:
    """
    A DataLoader class responsible for the user interface.

    This class manages user requests for specific data periods and universes, directing 
    these requests to the appropriate data source Reader. Upon receiving the data from 
    the Reader, the DataLoader transforms it into the format requested by the user and 
    applies any specified options.
    """    
    def __init__(
            self, 
            source: str, 
            start_date: str, 
            end_date: str=None, 
            universe: Union[list, np.ndarray]=None
            ) -> None:
        """
        Initializes the DataLoader with the specified parameters for loading 
        financial data.

        Parameters:
        - source (str): The source identifier from which to load data.
        - start_date (str): The starting date for the data loading period.
        - end_date (str, optional): The ending date for the data loading period. 
          Defaults to None.
        - universe (Union[list, np.ndarray], optional): The universe of stock IDs to be loaded. 
          This can be a list or numpy array, containing elements that are either strings 
          or integers. The format of stock IDs can vary; a separate utility function 
          will standardize them for consistency. Defaults to None.
        
        Note:
        Stock ID formats in the 'universe' (either strings or integers in a list or numpy array) 
        are automatically standardized by a common utility function to ensure consistency and 
        compatibility with the data source.
        """        
        pass

    def get_data(
            self, 
            data: Union[str, List[str]],
            download=True,
    ) -> pd.DataFrame:
        """
        Retrieves financial data specified by the 'data' parameter and returns it 
        as a pandas DataFrame. The structure of the returned DataFrame depends on 
        the type of the 'data' parameter.

        If 'data' is a single string denoting the data name, the method returns a 
        DataFrame with dates as index rows and stock identifiers as columns.

        If 'data' is a list of strings representing multiple data names, the method 
        returns a DataFrame with a MultiIndex (dates, stock identifiers) for the rows 
        and the different data names (such as PER, PBR, volume, etc.) as columns.

        Parameters:
        - data (Union[str, List[str]]): A single data name or a list of data names.
        - download (bool, optional): If True, attempts to download the data if not 
        available locally. Defaults to True.

        Returns:
        - pd.DataFrame: A DataFrame structured according to the input:
            - Single string 'data': Index = dates, Columns = stock IDs.
            - List of strings 'data': MultiIndex Rows = (dates, stock IDs), Columns = data names.
        """        
        pass


