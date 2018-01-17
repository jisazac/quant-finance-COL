class simple_interet:
    def __init__(self,rate, periodicity,currency="COP"):
        self.rate=rate
        self.period=periodicity
        self.currenc=currency

    def __str__(self):
        display = str(self.rate)+"%"+" "+"de tasa de interes simple"+"\n"
        display += "Con periodiciad:"+" "+str(self.period)+"\n"
        display += "Expresado en "+self.currenc
        return display

class time_of_investment:
    def __init__(self,number_of_periods,periodicity):
        self.number_of_periods=number_of_periods
        self.period=periodicity

    def __str__(self):
        return "La inversion se da durante: "+str(self.number_of_periods)+" "+str(self.period)


if __name__ == '__main__':
    i1=simple_interet(0.03,"month")
    print (i1)
    t=time_of_investment(3,"month")
    print (t)