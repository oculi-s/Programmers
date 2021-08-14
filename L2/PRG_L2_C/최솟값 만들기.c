#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int A[], size_t A_len, int B[], size_t B_len) {
	int n = 0;
	int a, ta, tb;
	int *ts, *o;
	while (A_len) {
		for (o = A, a = A_len, ts = A;a--;A++)
			ts = (*A > *ts) ? A : ts;
		ta = *ts;
		for (a = A_len - (ts - o), A = ts; a--;*A = *(A + 1), A++);
		A -= A_len;

		for (o = B, a = A_len, ts = B;a--;B++)
			ts = (*B < *ts) ? B : ts;
		tb = *ts;
		for (a = A_len - (ts - o), B = ts; a--;*B = *(B + 1), B++);
		B -= A_len;

		n += ta * tb;
		A_len--;
	}
	return n;
}

int main() {
	int A[3] = { 1,4,2 };
	int B[3] = { 5,4,4 };
	int t = solution(A, 3, B, 3);
	printf("%d", t);
}