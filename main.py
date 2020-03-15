from abc import ABC, abstractmethod
from random import sample, randint

class IMenu(ABC):
  @abstractmethod
  def create_menu(self):
    pass
  
class ScallopMenu(IMenu):
  def create_menu(self):
    self.menu = 'Scallops is the main course'

class VegitarianMenu(IMenu):
  def create_menu(self):
    self.menu = 'Veggies is the main course'

class KingCrabMenu(IMenu):
  def create_menu(self):
    self.menu = 'King Crab is the main course'

class ExperimentalMenu(IMenu):
  def create_menu(self):
    self.menu = 'The main course is a mystery'

class Restaurant:
  desired_ingredients = []
  ingredients = []
  bad_ingredients = []
  menu = 'No menu!'

  def __init__(self, desired_ingredients = []):
    self.desired_ingredients = desired_ingredients

  def filter_bad_ing(self, query):
    return query not in self.bad_ingredients

  def source_ingredients(self):
    start = 0
    end = randint(3, 5)
    self.ingredients = self.desired_ingredients[start:end]

  def evaluate_ingredients(self):
    ingredients = self.ingredients
    remove_bad = self.filter_bad_ing
    self.bad_ingredients = []
    self.ingredients = filter(remove_bad, ingredients)

  def create_menu(self):
    self.menu = 'No Menu!'
  

def main():
  desired_ingredients = [
    'scallops',
    'hake',
    'razor clams',
    'langoustines',
    'ginkgo nuts',
    'sweet onions',
    'pine mushrooms',
    'quail'
  ]
  print(desired_ingredients)

main()

