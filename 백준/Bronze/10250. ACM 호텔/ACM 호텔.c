#include <stdio.h>

int main() 
{ 
	int t, h, w, n;
	scanf("%d", &t);
	for (; t--;) {
		scanf("%d %d %d", &h, &w, &n);
		if (n % h == 0)
			printf("%d\n", h * 100 + (n / h));
		else
			printf("%d\n", (n % h) * 100 + (n / h) + 1);
	}
	return 0;
}