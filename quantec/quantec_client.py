from pkg_resources import get_distribution


class QuantecClient(object):
    """Initialization method of the :code:`QuantecClient` class.

    Parameters
    ----------
    apikey : str
        API key to use.
    respformat : str, optional
        Return `csv` or `json` in result (default csv)
    is_tidy : logical, optional
        Return data in tidy format (default TRUE)

    Returns
    -------
    Class
        QuantecClient Class
    """

    def __init__(self, **kwargs):
        __version__ = get_distribution("quantec").version

        kwargs.setdefault("respformat", "csv")
        kwargs.setdefault("is_tidy", True)

        self.apikey = kwargs["apikey"]
        self.respformat = kwargs["respformat"]
        self.is_tidy = kwargs["is_tidy"]

    from ._get_data import get_data
