from event import event
import random

class turbulence(event):
  def __init__(self, period):
    self.period = period

  def change(self):
    return (self.period/15) * random.gauss(0, 180)
