from math import cos, pi


class Arbitration:
    def __init__(self, time_to_collision, delta_time):
        self.time_to_collision = time_to_collision
        self.delta_time = delta_time
        self.h_control_value = 1.0
        self.c_control_value = 0.0

    def compute_sharing_value(self, time_gap):
        if time_gap > self.time_to_collision + self.delta_time:
            return self.h_control_value
        if self.time_to_collision - self.delta_time <= time_gap <= self.time_to_collision + self.delta_time:
            return 0.5 * (1 - cos(0.5 * pi / self.delta_time * (time_gap - (self.time_to_collision - self.delta_time))))
        if self.time_to_collision - self.delta_time < time_gap:
            return self.c_control_value
