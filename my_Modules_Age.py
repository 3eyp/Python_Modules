import datetime

# Modules Age calculation

class My_Age():
    def __init__(self):
        pass
    def age(self):
        now = datetime.datetime.now().year
        age = int(input("Age: "))
        if now <= 0:
            return
        return now - age



