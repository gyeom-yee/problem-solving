#include <stdio.h>

void star(int n, int x, int y) {
	if ((x / n) % 3 == 1 && (y / n) % 3 == 1)
		printf(" ");
	else {
		if (n / 3 == 0)
			printf("*");
		else
			star(n / 3, x, y);
	}
}

int main() {
	int n, i, j;
	scanf("%d", &n);
	for (j = 0; j < n; j++) {
		for (i = 0; i < n; i++)
			star(n, i, j);
		printf("\n");
	}
	return 0;
}