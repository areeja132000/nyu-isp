// Code assumes that input will include only positive integers
// Code also assumes that input will have at most 15 integers
// I am not sure why we are using arrays. Could just get max and min as we are getting input

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
  char input[401];
  char exit_key[3] = "q\n";
  char *success;
  int num_values = 0;
  int min_value = -1;
  int max_value = -1;
  int *arr_ptr;

  arr_ptr = (int *)malloc(15 * sizeof(int)); //at most 15 integers
  if(arr_ptr == NULL) { 
    perror("Failed to allocate memory for int array\n"); 
    exit(1); 
  }

  printf("Please enter the series of integers for which you would like to find the minimum and maximum.\nInput the integers by writing them out and pressing enter. Press 'q' to quit anytime.\n");

  while (strcmp(input, exit_key)) {
    printf("Integer %d: ", num_values+1);
    success = fgets(input, 401, stdin);
    if (success == NULL) {
      perror("Failed to read input integer\n"); 
      exit(1); 
    }
    if (strcmp(input, exit_key)) {
      arr_ptr[num_values] = atoi(input);
      num_values+=1;
    }
  }

  int i;
  for (i=0; i<num_values; i++) {
    if (arr_ptr[i] > max_value) {
      max_value = arr_ptr[i];
    }

    if (i == 0) {
      min_value = arr_ptr[i];
    } else {
      if (arr_ptr[i] < min_value) {
        min_value = arr_ptr[i];
      }
    }
  }

  free(arr_ptr);
  printf("Numbers entered: %d\nMinimum number is: %d\nMaximum number is: %d\n", num_values, min_value, max_value); 
}



