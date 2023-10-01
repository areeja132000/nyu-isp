// Code assumes that input will include only positive integers
// Code also assumes that input is properly formatted
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
  char *string; 
  size_t string_size = 401; //In actuality, 1 size less
  char *success;

  string = (char *)malloc(string_size * sizeof(char)); 
  if(string == NULL) { 
    perror("Failed to allocate memory for buffer\n"); 
    exit(1); 
  }

  printf("Please enter the series of integers (separated by ',') for which you would like to find the minimum and maximum (Example input: '1,2,2,3,4,5,67,7,5'): ");
  success = fgets(string, string_size , stdin);

  if (success == NULL) {
    perror("Failed to read input\n"); 
    exit(1); 
  } else {
 
    int max_value = -1;
    int min_value = -1;
    int num_values = 0;
    char *save_ptr;
    char *token = strtok_r(string, ",", &save_ptr); 

    while (token != NULL) {
      num_values+=1; 

      if (atoi(token) > max_value) {
        max_value = atoi(token);
      }

      if (num_values == 1) {
        min_value = atoi(token);
      } else {
        if (atoi(token) < min_value) {
          min_value = atoi(token);
        }
      }

      token = strtok_r(NULL, ",", &save_ptr); 
    }
    printf("Numbers entered: %d\nMinimum number is: %d\nMaximum number is: %d\n", num_values, min_value, max_value); 
  }
  free(string);
}



