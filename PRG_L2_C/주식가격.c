#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int prices[], size_t prices_len) {
    int n = prices_len;
    int* answer = (int*)malloc(n*sizeof(int)+1);
    int i, j, x;
    bool c;
    for (i=0; i<n; i++){
        c = true;
        x = *(prices+i);
        for (j=i+1;j<n;j++){
            if (x>*(prices+j)){
                c = false;
                break;
            }
        }
        *(answer + i) = j-i-(c|(j>n));
    }
    *(answer + n) = NULL;
    return answer;
}