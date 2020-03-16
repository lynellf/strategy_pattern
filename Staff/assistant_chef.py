class AssistantChef:
  _course = None
  course = 'No Main Course!'

  def __init__(self, course, ingredients = [], strategies = []):
    self._course = course(None)
    self.select_course(ingredients, strategies)

  def select_course(self, ingredients, strategies):
    for strategy in strategies:
      strategy.apply_strategy(self._course, ingredients)

  def get_main_course(self):
    self.course = self._course.get_course()
    return self.course