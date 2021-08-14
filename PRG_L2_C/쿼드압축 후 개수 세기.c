#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool s(int **a, int x) {
	for (int i = 0;i < x;i++)
		for (int j = 0;j < x; j++)
			if (a[i][j] != a[0][0])
				return false;
	return true;
}

void f(int **a, size_t r, int* b) {
	int x, y, i, j, **c;

	if (r == 2) {
		if (s(a, 2)) {
			b[a[0][0]]++;
		}
		else {
			for (i = 0; i < 2; i++)
				for (j = 0; j < 2; j++)
					b[a[i][j]]++;
		}
	}
	else {
		c = malloc(sizeof(int*)*r / 2);
		for (int i = 0; i < r / 2; i++)
			c[i] = malloc(sizeof(int) * r / 2);
		for (y = 0;y < 2;y++) {
			for (x = 0;x < 2;x++) {
				for (i = 0; i < r / 2; i++)
					for (j = 0; j < r / 2; j++)
						c[i][j] = a[y * r / 2 + j][x * r / 2 + i];
				s(c, r / 2) ? b[c[0][0]]++ : f(c, r / 2, b);
			}
		}
	}
}

int* solution(int** arr, size_t arr_rows, size_t arr_cols) {
	int * answer = malloc(sizeof(int) * 3);
	answer[0] = 0;
	answer[1] = 0;
	s(arr, arr_rows) ? answer[**arr] ++ : f(arr, arr_rows, answer);
	return answer;
}

int main() {
	int n = 8;
	int arr[4][4] = { {1, 1, 0, 0}, {1, 0, 0, 0}, { 1, 0, 0, 1}, { 1, 1, 1, 1 } };
	int arr[8][8] = { {1,1,1,1,1,1,1,1},{0,1,1,1,1,1,1,1},{0,0,0,0,1,1,1,1},{0,1,0,0,1,1,1,1},{0,0,0,0,0,0,1,1},{0,0,0,0,0,0,0,1},{0,0,0,0,1,0,0,1},{0,0,0,0,1,1,1,1} };
	int **a = malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++) {
		a[i] = malloc(sizeof(int) * n);
		for (int j = 0; j < n; j++)
			a[i][j] = arr[i][j];
	}

	int *answer = malloc(sizeof(int) * 2);
	answer = solution(a, n, n);
	printf("%d %d", answer[0], answer[1]);
}