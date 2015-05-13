# This code utilizes Python 3.4.1

def stringcases(string):
  """
  This function that akes a string and returns 
  a tuple of four versions of the string: 
  uppercased, lowercased, titlecased 
  (where every word's first letter is capitalized), 
  and a reversed version of the string.
  """
  
  words = string.split() #These five lines will make the first
  capitalized_words = [] #letter of each word capitalized.
  for word in words:
    title_case_word = word[0].upper() + word[1:]
    capitalized_words.append(title_case_word)
  title_case = ' '.join(capitalized_words)

  reversed_string = string[::-1] #This will reverse the string
    
  cases = (string.upper(), string.lower(),
           title_case, reversed_string)
  return cases
