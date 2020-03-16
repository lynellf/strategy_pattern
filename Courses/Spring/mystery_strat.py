from strat_interface import IStrategy

class MysteryStrat(IStrategy):
  def apply_strategy(self, course, ingredients):
    has_no_ingredients = len(ingredients) == 0
    if has_no_ingredients:
      course.set_strategy(self.define_main_course)
      
  def define_main_course(self):
    return 'The main course is an exerpiment'