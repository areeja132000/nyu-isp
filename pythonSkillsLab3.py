import math 

def return_max(int_list):
  
  if len(int_list) != 1:
    pivot = int(math.ceil(len(int_list)/2.0))
    max_left_of_partition = return_max(int_list[:pivot])
    max_right_of_partition = return_max(int_list[pivot:])
    if max_left_of_partition > max_right_of_partition:
      return max_left_of_partition
    else:
      return max_right_of_partition
  else:
    return int_list[0]

if __name__ == "__main__":

  input_nums = input("Please enter the list of numbers (seperated by a ',') that you would like to find the maximum value of: ")

  int_list_raw = input_nums.split(',')
  int_list_cleaned=  []

  for i in range(len(int_list_raw)):
    if not int_list_raw[i].isnumeric():
      print("One of the values entered into the list is not a number")
      exit()
    else:
      int_list_cleaned.append(int(int_list_raw[i]))

  print("The maximum value is " + str(return_max(int_list_cleaned)))




