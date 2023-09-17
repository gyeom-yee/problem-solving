#include <stdio.h>

int main()
{
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	if (c <= b)
		printf("%d\n", -1);
	else
		printf("%d\n", a / (c - b) + 1);
	return 0;
}