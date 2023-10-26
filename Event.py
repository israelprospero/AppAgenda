from datetime import datetime

class Event:

    def __init__(self, title: str, date: str, time: str, reminder: int) -> None:
        assert len(title) > 0, "The title of the event can't be empty!"
        assert reminder >= 0, f'You have to define a valid reminder!' 
        
        self.title = title
        self.date = datetime.strptime(date, '%d/%m/%Y').date()
        self.time = datetime.strptime(time, '%H:%M').time()
        self.reminder = reminder    # minutes before event

    def formatDate(self):
        pass