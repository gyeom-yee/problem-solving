#include <stdio.h>

int main()
{
	int a, b, c;
	int count = 0;
	int i, j;
	char str[10];
	char x[10] = { '0','1','2','3','4','5','6','7','8','9' };

	scanf("%d %d %d", &a, &b, &c);
	sprintf(str, "%d", a*b*c);

	for (i = 0; i < 10; i++) {
		for (j = 0; j < 10; j++) {
			if (str[j] == x[i]) {
				count++;
			}	
		}
		printf("%d\n", count);
		count = 0;
	}
	return 0;
}