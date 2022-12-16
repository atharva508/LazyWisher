# A class that defines a general structure for an event
from datetime import date
class WishingDate:

    relation = None
    name  = None
    event = None
    event_day = None
    event_month = None

    def __init__(self,relation,name,event,event_day,event_month):
        self.relation = relation
        self.name = name
        self.event = event
        self.event_month = event_month
        self.event_day = event_day
    
