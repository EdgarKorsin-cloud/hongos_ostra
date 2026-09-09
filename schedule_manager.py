import datetime

class Scheduler:
    def __init__(self):
        self.incubation_period=0

    def incubation_end(self,date):
        incubation_start= datetime.datetime.strptime(date, '%Y-%m-%d')
        incubation_end = incubation_start + datetime.timedelta(days=30) #change to days=var where var is days of product_type
        return incubation_end.strftime('%Y-%m-%d')

    def fructification(self,incubation_end_date):
        start= datetime.datetime.strptime(incubation_end_date, '%Y-%m-%d')
        fructification_start= start + datetime.timedelta(days=7)
        harvest = fructification_start + datetime.timedelta(days=3)
        return harvest.strftime('%Y-%m-%d')
    
