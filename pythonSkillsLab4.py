# Code assumes that input list contains only numbers (negative and positive acceptable)
# Code also assumes numpy is installed

import numpy as np

def remove_duplist(input_list):
  output_list = []
  
  for item in input_list:
    if item not in output_list:
      output_list.append(item)

  output_list.sort()
  return output_list

def create_set(input_list):
  output_list=list(set(input_list))
  output_list.sort()
  return output_list

def create_keys(input_list):
  output_list=list(dict.fromkeys(input_list))
  output_list.sort()
  return output_list

def numpy_unique(input_list):
  output_list=list(np.unique(input_list))
  output_list.sort()
  return output_list

if __name__ == "__main__":

  input_items = input("Please enter the list of items (seperated by a ',') that you would like to remove duplicates for: ")

  int_list_raw = input_items.split(',')
  input_list = []

  for i in range(len(int_list_raw)):
    input_list.append(int(int_list_raw[i]))

  print("List with duplicates removed (with method 1): " + str(remove_duplist(input_list)))
  print("List with duplicates removed (with method 2): " + str(create_set(input_list)))
  print("List with duplicates removed (with method 3): " + str(create_keys(input_list)))
  print("List with duplicates removed (with method 4): " + str(numpy_unique(input_list)))




