class Clock(object):
    def __init__(self, time):
        self.time = time
        print(time)
        print(self.time)
    def print_time(self):
        time = '6:30'
        print(time)
        print(self.time)

clock = Clock('5:30')
clock.print_time()