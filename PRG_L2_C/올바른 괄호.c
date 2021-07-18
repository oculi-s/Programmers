#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(const char* s) {
	int n = 0;
	for (;*s; s++) {
		n += (*s == 40) ? 1 : -1;
		if (n < 0)
			return false;
	}
	return !n;
}

int main() {
	const char s[] = ")(";
	int t = solution(s);
	printf(t ? "true" : "false");
}