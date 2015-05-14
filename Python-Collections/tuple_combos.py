# Created using Python 3.4.1

# combo(['swallow', 'snake', 'parrot'], 'abc')
# Output:
# [('swallow', 'a'), ('snake', 'b'), ('parrot', 'c')]

def combo(my_list, string):
  """
  This function takes two strings, list, or a
  combination of both and produces a list of 
  tuples that is a combination of the two.
  """

  index = 0
  new_list = []
    
  first = list(my_list)
  second = list(string)
    
  for each in first:
    new_list.append((each, second[index]))
    index += 1
    
  return  new_list

print(combo(['swallow', 'snake', 'parrot'], 'abc'))
