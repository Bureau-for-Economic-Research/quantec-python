import requests
import logging
import pandas as pd
from datetime import date
from typing import Union
from io import StringIO

log = logging.getLogger(__name__)


def get_data(
    self,
    time_series_code: str,
    freq: str = "M",
    start_year: str = "1900",
    end_year: str = date.today().strftime("%Y"),
) -> Union[pd.DataFrame, dict]:
    """
    Fetch data from Quantec's API.

    Parameters
    ----------
    time_series_code : str
        Code representing the time series to be fetched.
    freq : str, optional
        Frequency of the data. Can be 'M', 'Q', etc. Defaults to 'M'.
    start_year : str, optional
        Start date for the data to be fetched in the format 'YYYY-MM-DD'. Defaults to '1900-01-01'.
    end_year : str, optional
        End date for the data to be fetched in the format 'YYYY-MM-DD'. Defaults to today's date.

    Returns
    -------
    Union[pd.DataFrame, dict]
        If the data fetched is in CSV format, a pandas DataFrame is returned.
        If the data fetched is in JSON format, a dictionary is returned.

    Raises
    ------
    HTTPError
        If there's an HTTP error in the request.
    """

    url = "https://www.easydata.co.za/api/v3/download/"

    query_params = {
        "timeSeriesCodes": time_series_code,
        "respFormat": self.respformat,
        "freqs": freq,
        "startYear": start_year,
        "endYear": end_year,
        "isTidy": self.is_tidy,
    }

    log.debug(f"[{time_series_code}] -- Querying with parameters: [{query_params}]")

    query_params["auth_token"] = self.apikey

    response = requests.get(url, params=query_params)
    response.raise_for_status()

    if self.respformat == "csv":
        out = pd.read_csv(StringIO(response.text)).dropna().reset_index()

    else:
        out = response.json()  # Assuming JSON format if not CSV

    log.debug(f"[{time_series_code}] -- Found {len(out)} rows")

    return out
