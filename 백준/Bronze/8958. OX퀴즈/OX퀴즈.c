#include<stdio.h>

int main() 
{
	int n, i, j, count = 0, sum;
	char str[85];

	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%s", str);
		for (count = 0, sum = 0, j = 0; j < strlen(str); j++) {
			if (str[j] == 'O') {
				count++;
				sum += count;
			}
			else if (str[j] == 'X')
				count = 0;
		}
		printf("%d\n", sum);
	}
}