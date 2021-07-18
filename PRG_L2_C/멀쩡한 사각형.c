#include <stdio.h>
#include <stdlib.h>

long long solution(long long w, long long h) {
	long long answer = w * h - (w + h);
	long long t;
	if (w > h) {
		t = h;
		h = w;
		w = t;
	}
	while (h % w) {
		h %= w;
		t = h;
		h = w;
		w = t;
	}
	answer += w;
	return answer;
}