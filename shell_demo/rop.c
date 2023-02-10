#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char dummy[1000] = "";

void vuln()
{
    char buffer[64];
    printf("Enter text\n");

    fgets(buffer, 10000, stdin);
    // strcpy(buffer, s);
}

int main(int argc, char **argv)
{
    // if (argc == 1) {
        // fprintf(stderr, "Enter a string!\n");
        // exit(EXIT_FAILURE);
    // }
    vuln();
    printf("Done!\n");
}
