#include <stdio.h>

int main() {
    char s[] = "  He  llo   wor  ld   ";
    int n = 22;

    // char s[] = "  He  ";
    // int n = 6;

    // char s[] = "      ";
    // int n = 6;

    int i = 0;
    int last_space = 1;

    for (int j = 0; j < n; j++) {
        if (s[j] == ' ' && last_space) continue;

        s[i] = s[j];
        if (s[j] == ' ' && !last_space) last_space = 1;
        if (s[j] != ' ' && last_space) last_space = 0;
        i++;
    }

    if (s[i - 1] == ' ') i--;
    s[i] = 0;

    printf("\n%s", s);
    return 0;
}