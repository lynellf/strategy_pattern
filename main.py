from abc import ABC, abstractmethod
from random import sample, randint

# Helper Methods
def slice(arr = [], start = 0, end = 0):
  return arr[start:end]

def is_in(query, population):
    return query in population

class IStrategy(ABC):
  @abstractmethod
  def apply_strategy(self):
    pass

  @abstractmethod
  def define_main_course(self):
    pass
  
class ScallopsStrat(IStrategy):
  def apply_strategy(self, course, ingredients):
    if 'scallops' in ingredients:
      course.set_strategy(self.define_main_course)

  def define_main_course(self):
    return 'Scallops is the main course'

class VeggieStrat(IStrategy):
  def apply_strategy(self, course, ingredients):
    has_no_crab = 'king crab' not in ingredients
    has_no_scallops = 'scallops' not in ingredients
    has_no_meat = has_no_crab and has_no_scallops

    if has_no_meat:
      course.set_strategy(self.define_main_course)

  def define_main_course(self):
    return 'Veggies is the main course'

class CrabStrat(IStrategy):
  def apply_strategy(self, course, ingredients):
    has_crab = 'king crab' in ingredients
    has_no_scallops = 'scallops' not in ingredients
    if has_crab and has_no_scallops:
      course.set_strategy(self.define_main_course)
      
  def define_main_course(self):
    return 'King Crab is the main course'

class MysteryStrat(IStrategy):
  def apply_strategy(self, course, ingredients):
    has_no_ingredients = len(ingredients) == 0
    if has_no_ingredients:
      course.set_strategy(self.define_main_course)
      
  def define_main_course(self):
    return 'The main course is an exerpiment'
class Course:
  course = 'No main course!'
  _strategy = None

  def __init__(self, strategy):
    self._strategy = strategy

  def strategy(self):
    pass
    
  def set_strategy(self, strategy):
    self._strategy = strategy

  def get_course(self):
    self.course = self._strategy()
    return self.course

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

class LeadChef:
  seasonal_ingredients = []
  ingredients = []
  bad_ingredients = []

  def __init__(self, seasonal_ingredients = []):
    self.seasonal_ingredients = seasonal_ingredients
    self.source_ingredients()
    self.check_ingredients()

  def source_ingredients(self):
    start = randint(0, len(self.seasonal_ingredients))
    end = randint(0, len(self.seasonal_ingredients))
    query = self.seasonal_ingredients
    self.ingredients = slice(query, start, end)

  def check_ingredients(self):
    maximum = len(self.ingredients)
    start = randint(0, maximum)
    end = randint(start, maximum)
    query = self.ingredients
    self.bad_ingredients = slice(query, start, end)
  
  def get_ingredients(self):
    return self.ingredients

def main():
  seasonal_ingredients = [
    'scallops',
    'hake',
    'razor clams',
    'langoustines',
    'ginkgo nuts',
    'sweet onions',
    'pine mushrooms',
    'quail',
    'king crab'
  ]

  strategies = [
    ScallopsStrat(),
    VeggieStrat(),
    CrabStrat(),
    MysteryStrat()
  ]

  fredrick = LeadChef(seasonal_ingredients)
  ingredients = fredrick.get_ingredients()
  orjan = AssistantChef(Course, ingredients, strategies)
  todays_main_course = orjan.get_main_course()
  
  print(todays_main_course, ingredients)

main()

