#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(const char* s) {
    int i,j;
    while(*(s+ ++i)!=NULL){}
    while((int)*(s+ ++j))
    bool answer = ((i==4)||(i==6))&&(j==i);
    return answer;
}