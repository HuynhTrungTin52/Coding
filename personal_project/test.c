// C program to illustrate how to generate random number
// withing a range
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
	time_t seconds;
	seconds = time(NULL);
	srand(seconds);
    // Set the upper bound for random numbers
    int upper_bound = 10;
    // Set the lower bound for random numbers
    int lower_bound = 1;

    // Loop through 10 times
    for (int i = 0; i < 10; i++) {
        // Generate a random number within the specified
        // bounds
        int value = rand() % (upper_bound)
                    + lower_bound;
        // Print the generated random value
        printf("%d ", value);
    }

    return 0;
}