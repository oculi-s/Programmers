#include<stdio.h>
#include<stdlib.h>

void cpy(char *a, size_t n, const char *b)
{
	for (; (*a = *b) && (n); a++, b++, n--);
}

char* solution(const char *number, long k) {
	long n = 0;
	while (*(number + ++n)) {}

	long d = n - k;
	char *p = (char*)malloc(n * sizeof(char));
	cpy(p, n, number);

	long a, b, t;
	for (a = 0; a < d; a++) {
		for (b = a, t = a; b <= a + k; b++)
			if (*(p + b) > *(p + t))
				t = b;
		if (t != a) {
			cpy(p + a, n - t + a, p + t);
			k -= t - a;
		}
	}
	*(p + d) = NULL;
	return p;
}