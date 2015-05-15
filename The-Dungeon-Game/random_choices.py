import random
my_iterable = [(1, 2), (3, 7), (4, 9), (11, 3)]


def nchoices(my_iterable, my_integer):
  """
  This function creates a list of random
  iterables based off of a list of iterables
  (my_iterable) and n number of items to be in 
  the new list (my_integer)
  """

  random_list = []
  integer_list = list(range(1, my_integer + 1))
  
  for each_number in integer_list:
    random_list.append(random.choice(my_iterable))
    
  return random_list
