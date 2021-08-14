#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
    long long answer = 0;
    int c = a>b ? b:a;
    int d = a<b ? b:a;
    for (int i=c; i<=d; i++)
        answer += i;
    return answer;
}