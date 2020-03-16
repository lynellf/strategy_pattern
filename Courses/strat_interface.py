from abc import ABC, abstractmethod

class IStrategy(ABC):
  @abstractmethod
  def apply_strategy(self):
    pass

  @abstractmethod
  def define_main_course(self):
    pass