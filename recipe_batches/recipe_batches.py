#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 1000
  
  # if batches == 0: 
  #   return 0 
  for a in ingredients.keys():
    #if ingredient isn't in the recipe ingre
    # print(a, ingredients)
    if a not in ingredients:
      
      return 0
    if ingredients[a] > recipe[a]:
      quantity = ingredients[a] // recipe[a]
      if quantity < batches:
        batches = quantity
    
    # elif recipe[a] < ingredients[a]:
    #   return 0

     
  # else:
  #   return 0

  return batches

print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }))


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))