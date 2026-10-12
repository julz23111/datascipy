import random
from pythonds3.basic import Queue


class Runway:
    def __init__(self, landing_seconds):
        self.landing_seconds = landing_seconds
        self.current_aircraft = None
        self.time_remaining = 0

    def tick(self):
        if self.current_aircraft is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_aircraft = None

    def busy(self):
        return self.current_aircraft is not None

    def start_next(self, new_aircraft):
        self.current_aircraft = new_aircraft
        self.time_remaining = self.landing_seconds

class Aircraft:
    def __init__(self, arrival_time):
        self.timestamp = arrival_time
        self.flightid = random.randint(1, 9999)

   
    def get_stamp(self):
        return self.timestamp

  

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulation(num_seconds, landing_seconds):
    runway = Runway(landing_seconds)
    landing_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_landing_request():
            aircraft = Aircraft(current_second)
            landing_queue.enqueue(aircraft)

        if (not runway.busy()) and (not landing_queue.is_empty()):
            next_aircraft = landing_queue.dequeue()
            waiting_times.append(next_aircraft.wait_time(current_second))
            runway.start_next(next_aircraft)

        runway.tick()

    average_wait = (
        sum(waiting_times) / len(waiting_times)
        if waiting_times else 0
    )
    print(
        f"Average wait: {average_wait / 60:.1f} min | "
        f"Aircraft remaining: {landing_queue.size()}"
    )


def new_landing_request():
    num = random.randrange(1, 181)
    return num == 180


for i in range(10):
    simulation(3600, 10*60)  # 10 minutes in seconds
