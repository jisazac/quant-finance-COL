# stock_class.py


class stock:
    """Class for ordinary stock """

    def __init__(self,ticker,price,dvd_yield,hist_data):
        self.ticker=ticker
        self.price=price
        self.dvd_yield=dvd_yield
        self.hist_data=hist_data


    def retorno(self,log=False):
        precios=self.hist_data["PX_LAST"]
        return (precios[-1]-precios[0])/precios[0]


