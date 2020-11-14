
import random
from plane import plane
from environment import environment
import logging
import time





if __name__ == "__main__":
  flying_machine1 = plane(0.9,"Boening 404")
  flying_machine2 = plane(0.5,"Unit Under Test 1")
  flying_machine3 = plane(0.0,"No Need Of Correction Plane")
  planes_under_test = [flying_machine1, flying_machine2, flying_machine3]

  period = 0.1
  time_stamps = 2000


  test_environment = environment(period,planes_under_test)

  file_logger = logging.getLogger("Data Logger")
  logging.basicConfig(filename='data.log',filemode='w', level=logging.INFO)

  print("Starting simulation\n")

  print("Logging simulation data, please wait...")
  env_info=[]
  for i in range(time_stamps):
    env_info += test_environment.next_time_stamp()

  for info in env_info:
    logging.info(info)



  print("\nEnding simulation")