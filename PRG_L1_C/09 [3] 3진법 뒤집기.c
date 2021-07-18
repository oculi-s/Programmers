#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int solution(int n) {
	int answer = 0;
	int* n3 = (int*)malloc(n);
	int i = 0;
	while (n >= 1){
		*(n3 + i) = n % 3;
		n = (int)(n/3);
		i++;
	}
	for (int j=0; j<i; j++)
		answer += *(n3+(i-j-1)) * pow(3, j);
	return answer;
}

int main() {
	printf("%d", solution(45));
}