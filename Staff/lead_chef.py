from random import randint
from dependencies.helpers import slice

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
