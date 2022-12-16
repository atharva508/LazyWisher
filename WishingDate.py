# A class that defines a general structure for an event
from datetime import date
class WishingDate:

    relation = None
    name  = None
    event = None
    event_date = None

    def __init__(self,relation,name,event,event_day,event_month):
        self.relation = relation
        self.name = name
        self.event = event
        self.event_date = date(2022,event_month,event_day)
    
