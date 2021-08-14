#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int* solution(int numbers[], size_t numbers_len) {
    int* answer = (int*)malloc(sizeof(int) * numbers_len * 8);
    for (int i = 0; i < numbers_len * 2; i++) {
        *(answer + i) = 0;
    }
    int c = 0;
    for (int i = 0; i < numbers_len; i++) {
        for (int j = i + 1; j < numbers_len; j++) {
            int number = *(numbers + i) + *(numbers + j);
            bool go = true;
            for (int k = 0; k < c; k++) {
                if (number == *(answer + k)) {
                    go = false;
                    break;
                }
            }
            if (go) {
                for (int l = 0; l < c; l++) {
                    if (*(answer + l) > number) {
                        for (int m = c; m >= l; m--) {
                            *(answer + (m + 1)) = *(answer + m);
                        }
                        *(answer + l) = number;
                        go = false;
                        break;
                    }
                }
                if (go) {
                    *(answer + c) = number;
                }
                c++;
            }
        }
    }
    return answer;
}