from abc import abstractmethod, ABC



class event(ABC):
  def __init__(self):
    pass

  @abstractmethod
  def change(self,current_value:float):
    pass