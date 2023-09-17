#include <stdio.h>

int main() 
{ 
	int t, k, n;
	int y[14], sum;
	int i, j;
	
	scanf("%d", &t);
	for (; t--;) {
		scanf("%d", &k);
		scanf("%d", &n);
		for (i = 0; i < 14; i++)
			y[i] = i + 1;
		for (i = 0; i < k; i++) {
			for (sum = 0, j = 0; j < n; j++) {
				sum += y[j];
				y[j] = sum;
			}
		}
		printf("%d\n", sum);
	}
	return 0;
}