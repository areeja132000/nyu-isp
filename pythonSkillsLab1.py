import math

def print_function(palindrome):
  if palindrome:
    print("Your string is a palindrome\n")
  else:
    print("Your string is not a palindrome\n")


if __name__ == "__main__":
  input_string = input("Please enter your string: ")

  palindrome=True

  if len(input_string)==0:
    print_function(palindrome)
    exit()

  for i in range(int(math.ceil(len(input_string)/2.0))):
    if input_string[i] != input_string[len(input_string)-1-i]:
      palindrome=False
      break

  print_function(palindrome)



