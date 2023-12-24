from datetime import datetime

class Event:

    def __init__(self, title: str, date: str, time: str) -> None:
        assert len(title) > 0, "The title of the event can't be empty!"
        
        self.title = title
        self.date = datetime.strptime(date, '%d/%m/%Y').date()
        self.time = datetime.strptime(time, '%H:%M').time()

    def __repr__(self) -> str:
        return f'Event({self.title}, {self.date}, {self.time})'
