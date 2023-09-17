#include <stdio.h>

int h(int i) {
	if (i == 1000)
		return -1;
	int num[5];
	for (int j = 0; i; j++) {
		num[j] = i % 10;
		i /= 10;
	}
	return (num[1] - num[0] == num[2] - num[1]) ? 1 : -1;
}

int main() 
{
	int n, count = 0;
	scanf("%d", &n);
	if (n < 100)
		printf("%d\n", n);
	else {
		for (int i = 100; i <= n; i++) {
			if (h(i) == 1)
				count++;
		}
		printf("%d\n", 99 + count);
	}
	return 0;
}