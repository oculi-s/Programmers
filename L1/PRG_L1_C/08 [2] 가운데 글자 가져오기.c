#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* s) {
	int i = 0;
	while (*(s + ++i) != NULL) {
	}
	int a = (int)(((float)i - 1) / 2);
	int b = (int)((float)i / 2);
	char* answer = (char*)malloc(sizeof(char)*(b-a));
	for (i = 0; i <= b - a; i++) {
		*(answer + i) = *(s + i + a);
	}
	*(answer + i) = NULL;
	return answer;
}

int main() {
	printf("%s", solution("qwer"));
}
