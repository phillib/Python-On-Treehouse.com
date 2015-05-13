#Created using Python 3.4.1

def word_count(my_string):
  my_string = my_string.lower()
  my_string = my_string.split()
    
  dict_count = {}

  for word in my_string:
    if word not in dict_count:
      dict_count[word] = 1
    else:
      dict_count[word] = dict_count[word] + 1
  return dict_count

print word_count("This is a test and only a test")
