#include <stdio.h>

int main(){
    int selOption;
    printf("[1]Encrypt\n[2]Decrypt\n");
    printf("Choose a menu option, or press 0 to Exit: ");
    while (scanf("%d", &selOption) != 1) {
        printf("Choose a menu option, or press 0 to Exit: ");
        scanf("%d", &selOption);
    }
    scanf("%d", &selOption);
    printf("%d",selOption);
    return 0;
}