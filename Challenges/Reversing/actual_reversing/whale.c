#include "stdio.h"
#include "string.h"

void perscribe(char*);

char* TRUTH = "Can birds even understand me?";

int main(void)
{
    printf("Welcome to the transformer! We take what you have, and make it into what you have always wanted!\n");
    printf("What do you have to offer?\n> ");
    char buffer[64];
    fgets(buffer, 64, stdin);
    buffer[strcspn(buffer, "\n")] = '\0';

    // Calculate hamming distance
    int i = 0;
    int t = 0;
    while (buffer[i] != '\0') {
        char hold = buffer[i];
        while (hold) {
            t += hold & 1;
            hold >>= 1;
        }
        ++i;
    }

    // Check dist
    if (t != 108) {
        printf("That'll NEVER turn into what you want!\n");
        return 0;
    }

    printf("Here's my perscription:\n");
    perscribe(buffer);

    printf("%s", TRUTH);

    return 0;
}

// Starting with the MSB of the last char and moving forward
// Find the closest needed bit to that bit
void perscribe(char* input) {
    int cur;
    int len = strlen(TRUTH);
    int totallen = len << 3;
    // Stores held 1s
    char held[totallen];
    for (cur = 0; cur < len << 3; ++cur) {
        held[cur] = 0;
    }

    int len2 = strlen(input);

    // For each character in input
    for (cur = 0; cur < len2; ++cur) {
        // For each bit in the current char
        int i;
        for (i = 0; i < 8; ++i) {
            // Mask at bit i
            int m = 1 << i;
            int j;
            // Check if this bit is a 0
            if (!(input[cur] & m)) {
                continue;
            }

            // Get the nth bit of the input
            int curbit = (cur << 3) + i;

            for (j = 0;; ++j) {
                // If the jth bit of TRUTH has not been checked off yet, print out the difference of j and curbit
                if ((TRUTH[j >> 3] & (1 << (j & 7))) && !held[j]) {
                    printf("Take %d of these, then\n", j - curbit);
                    held[j] = 1;
                    break;
                }
            }
        }
    }

    printf("You're done!\n");
}
