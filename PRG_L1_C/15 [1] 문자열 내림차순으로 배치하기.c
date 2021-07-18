#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* s) {
    int l = 0;
    while (*(s+ ++l) != NULL){}
    char* answer = (char*)malloc(sizeof(char)*l);
    for (int i=0; i<l; i++){
        *(answer + i) = 0;
    }
    for (int i=0; i<l; i++){
        bool go = true;
        for (int j=i; j<l; j++){
            if (*(answer+j)<*(s+i)){
                *(answer + i) = *(s+i);
                go = false;
                break;
            }
        }
        if (go)
            *(answer + i) = *(s+i);
    }            
    return answer;
}