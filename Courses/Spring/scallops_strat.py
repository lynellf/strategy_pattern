from strat_interface import IStrategy

class ScallopsStrat(IStrategy):
  def apply_strategy(self, course, ingredients):
    if 'scallops' in ingredients:
      course.set_strategy(self.define_main_course)

  def define_main_course(self):
    return 'Scallops is the main course'
