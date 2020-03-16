from strat_interface import IStrategy

class CrabStrat(IStrategy):
  def apply_strategy(self, course, ingredients):
    has_crab = 'king crab' in ingredients
    has_no_scallops = 'scallops' not in ingredients
    if has_crab and has_no_scallops:
      course.set_strategy(self.define_main_course)
      
  def define_main_course(self):
    return 'King Crab is the main course'
