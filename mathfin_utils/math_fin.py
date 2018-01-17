import numpy as np
from mathfin_utils.simple_interest import simple_interest,time_of_investment

def caused_interest_simple(VP, t,t_frequency, interest,interest_frequency):
    """

    :param VP: float, monto invertido
    :param t:
    :param simple_interest:
    :return:
    """
    period=time_of_investment()
    period.period=t_frequency
    period.number_of_periods=t
    i=simple_interest()
    i.rate=interest
    i.period=interest_frequency
    return VP*period.number_of_periods*i.rate


def future_value_simple_interes(VP, t,t_frequency, interest,interest_frequency):
    """

    :param VP:
    :param t:
    :param t_frequency:
    :param interest:
    :param interest_frequency:
    :return:
    """
    period=time_of_investment()
    period.period=t_frequency
    period.number_of_periods=t
    i=simple_interest()
    i.rate=interest
    i.period=interest_frequency
    return VP*(1+period.number_of_periods*i.rate)


if __name__ == '__main__':
    print(caused_interest_simple(150000,5,"M",0.03,"M"))
    print (future_value_simple_interes(1000000,12,"M",0.01,"M"))
