from strat_interface import IStrategy

class VeggieStrat(IStrategy):
  def apply_strategy(self, course, ingredients):
    has_no_crab = 'king crab' not in ingredients
    has_no_scallops = 'scallops' not in ingredients
    has_no_meat = has_no_crab and has_no_scallops

    if has_no_meat:
      course.set_strategy(self.define_main_course)

  def define_main_course(self):
    return 'Veggies is the main course'
