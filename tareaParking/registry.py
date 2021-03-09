from datetime import datetime
import math

class Registry:
    def __init__(self, enter_time, license_plate):
        self.enter_time = enter_time
        self.license_plate = license_plate

    def time_in_parking(self):
        time = (self.out_time - self.enter_time)
        total_time = math.ceil(time.seconds/3600)
        return total_time

    def out_time (self):
        self.out_time = datetime.now()

    def payment(self, rate):
        return self.time_in_parking() * rate
