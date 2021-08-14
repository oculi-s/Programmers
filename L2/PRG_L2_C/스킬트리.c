#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* skill, const char* skill_trees[], size_t skill_trees_len) {
	int answer = skill_trees_len;
	int n = 0;
	int k, t;
	while (*(skill + ++n)) {}
	for (int i = 0; i < skill_trees_len; i++) {
		t = -2;
		for (int j = 0; j < n; j++) {
			k = 0;
			while ((*(*(skill_trees + i) + k) != NULL)&(*(skill + j) != *(*(skill_trees + i) -1 + ++k))) {}
			if (k - 2 < t) {
				answer--;
				break;
			}
			t = k - 2;
		}
	}
	return answer;
}