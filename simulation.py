import datetime

class clock:
    currentTime = datetime.datetime.now()
    @staticmethod
    def now():
        return clock.currentTime
    
    @staticmethod
    def advance():
        interval = datetime.timedelta(days=1)
        clock.currentTime += interval
        return interval
