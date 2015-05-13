# Created using Python 3.4.1

# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}


def most_classes(dictionary):
  """
  This function determines which key has
  the most values associated with it
  """
  max_count = 0
  most_classes = None
  for key,value in dictionary.items():
    teacher_value = len(value)
    if teacher_value > max_count:
      most_classes = key   
      max_count = teacher_value
  return(most_classes)


def num_teachers(dictionary):
  """
  This function will count the total 
  number of keys in a dictionary
  """
  total_teachers = 0
  for key in dictionary.items():
    total_teachers += 1
  return(total_teachers)


def stats(dictionary):
  """
  This function will show the total
  number of values associated with each key
  """
  teacher_list = []
  for key, value in dictionary.items():
    single_teacher = [key, len(value)]
    teacher_list.append(single_teacher)
  return teacher_list


def courses(dictionary):
  """
  This function will return a list of all
  of the values in a dictionary
  """
  all_courses = []
  for key, value in dictionary.items():
    total_courses = value
    for course in total_courses:
        all_courses.append(course)
  return all_courses
