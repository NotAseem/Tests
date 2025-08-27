#include <stdio.h>

int add(int a, int b) {
    return a + b + 5;
}

int main() {
    printf("Hello, World!\n");
    printf("add(1, 2) = %d\n", add(1, 2));
    return 0;
}
