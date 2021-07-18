#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int a, int b) {
	int day[] = { 31,29,31,30,31,30,31,31,30,31,30,31 };
	char *name[] = { "THU","FRI","SAT","SUN","MON","TUE","WED" };
	for (int i = 0; i < a-1; i++)
		b += day[i];
	char* answer = (char*)malloc(sizeof(char) * 3);
	answer = *(name + b % 7);
	return answer;
}

int main() {
	printf("%c", *solution(5, 24));
}