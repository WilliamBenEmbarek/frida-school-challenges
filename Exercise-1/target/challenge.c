#include <stdio.h>
#include <string.h>

void win() {
    printf("How did this happen!!! You win!");
}

int main() {
    char stringA[] = "Replace me!";
    char stringB[] = "TDCNETRULES!";    

    if(strcmp(stringA,stringB) == 0) {
        win();
    } else {
        printf("The strings are not equal\n");
    }
    return 0;
}