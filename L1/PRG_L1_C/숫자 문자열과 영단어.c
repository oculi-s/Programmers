#include <stdio.h>
#include <string.h>

int _cmp(char* a, char* b, int n) {
    for (int i = 0; i < n; i++)
        if (a[i] != b[i])
            return 0;
    return 1;
}

int solution(const char* s) {
    int i, j, v = 0, l[10] = { 4,3,3,5,4,4,3,5,5,4 };
    char n[10][6] = { "zero", "one", "two","three","four", "five", "six", "seven","eight", "nine" };
    for (i = 0; i < strlen(s); i++) {
        if (s[i] >= '0' && s[i] <= '9')
            v += s[i] - '0';
        else
            for (j = 0; j < 10; j++)
                if (_cmp(n[j], s + i, l[j]))
                    v += j, i += l[j] - 1;
        v *= 10;
    }
    return v / 10;
}