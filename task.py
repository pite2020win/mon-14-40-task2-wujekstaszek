
import random
class plane:
  def __init__(self,name="AirCraft",target=(0,0,0)):
    self.name=name
    self.orientation=[0,0,0]
    self.target=target
  def do_correction(self):
    i=0
    changed=[]
    length=len(self.orientation)
    while i<length:
      change = (self.target[i] - self.orientation[i])*0.2
      self.orientation[i]+=change
      i+=1
      changed.append(change)
    return changed


if __name__ == "__main__":
  flyingMachine1 = plane("Boening 404",[10,1,5])
  while 1:
    orientation=flyingMachine1.orientation
    correction=flyingMachine1.do_correction()
    target=flyingMachine1.target
    print(f'Current Orientation: {orientation},\ncorrection: {correction},\ntarget orientation:{target}')
    i=0
    while i<len(flyingMachine1.orientation): #turbulences
      flyingMachine1.orientation[i]+= random.gauss(-0.5, 0.5)
      i+=1
    print(f'Orientation after turbulences:{flyingMachine1.orientation}\n')