#include <stdio.h>
#include <math.h>

void move(int from, int to) {
	printf("%d %d\n", from, to);
}

void hanoi(int i,int from, int by, int to) {
	if (i == 1)
		move(from, to);
	else {
		hanoi(i - 1, from, to, by);
		move(from, to);
		hanoi(i - 1, by, from, to);
	}
}

int main() {
	int n;
	scanf("%d", &n);
	int cnt = pow(2, n) - 1;
	printf("%d\n", cnt);
	hanoi(n, 1, 2, 3);
	return 0;
}