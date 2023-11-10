from pkg_resources import get_distribution


class QuantecClient(object):
    """Initialization method of the :code:`QuantecClient` class.

    Parameters
    ----------
    apikey : str
        API key to use.

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

    from ._get_data import get_data
