from turbulence import turbulence
import logging

class environment:
  def __init__(self, period, planes):
    self.planes = planes
    self.period_in_sec = period
    self.turbulence = turbulence(self.period_in_sec)
    self.time_stamp = 0
  
  def next_time_stamp(self):
    to_return = []
    to_return.append(f"Current time stamp: {self.time_stamp}")
    self.time_stamp += 1
    current_turbulence=self.turbulence.change()
    for plane in self.planes:
      plane.do_a_correction()
      to_return.append(f'{plane.name}:\t{plane.roll}°')
      plane.roll += current_turbulence
    to_return.append(f'Current turbulence: {current_turbulence}°\n')
    return to_return