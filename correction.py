from event import event
import random

class correction(event):
  def __init__(self, procentage_force:float):
    self.procentage_force = procentage_force

  def change(self, current_value:float):
    return -(current_value*self.procentage_force*random.gauss(0.5,0.5))