#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n) {
	int* answer = (int*)calloc(n * (n + 1) / 2, sizeof(int));
	int i, j, k, t, o;
	k = 0;
	for (i = 0; i < n; i++) {
		t = (int)(i / 3);
		switch (i % 3) {
		case 0:
			o = 4 * t * (t + 1) / 2;
			break;
		case 1:
			o++;
			break;
		case 2:
			o -= n - t;
			break;
		}
		for (j = k; j < k + n - i; j++) {
			*(answer + o) = j + 1;
			
			if (j == k + n - i - 1)
				break;

			switch (i % 3) {

			case 0:
				o += (j - k) + 2 * t + 1;
				break;
			case 1:
				o++;
				break;
			case 2:
				o -= k + n - i - j + 2 * t + 1;
				break;
			}
		}
		k += n - i;
	}
	return answer;
}