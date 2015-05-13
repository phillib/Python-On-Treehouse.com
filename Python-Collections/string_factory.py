#Created using Python 3.4.1

#This will create a list of name and food pairs using the given string.
#Example:  "Hi, I'm Michelangelo and I love to eat PIZZA!"


dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(dicts, string):
  new_list = []
  for combo in dicts:
    new_list.append(string.format(**combo))
  
  return new_list
