#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ptrace.h>

void friendlyFunction() {
    if (ptrace(PTRACE_TRACEME, 0, NULL, 0) == -1) {
        printf("Debugger detected! Exiting...\n");
        exit(1);
    }
}

void encrypt(char *input) {
    char zOLTAN = 'P';
    
    for (size_t i = 0; i < strlen(input); i++) {
        input[i] = input[i] ^ zOLTAN;
        printf("%c", input[i]);
    }
    printf("\n");
}

int main() {
    friendlyFunction();
    char word[256];
    printf("What is ze passcode monsieur?\n");
    scanf("%255s", word);
    
    encrypt(word);
    
    if (strcmp(word, "brigade") == 0) {
        printf("correct password\n");
    } else {
        printf("wrong password\n");
    }
    
    return 0;
}
