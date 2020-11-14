from correction import correction
import random



class plane:
  def __init__(self,correction_unit_procentage_force:float,name="AirCraft"):
    self.name = name
    self.roll = random.gauss(0,180)
    self.correction_unit = correction(correction_unit_procentage_force)
    
  def do_a_correction(self):
    if self.roll > 180:
      self.roll -= 360
    elif self.roll < -180:
      self.roll += 360
    change = self.correction_unit.change(self.roll)
    self.roll += change