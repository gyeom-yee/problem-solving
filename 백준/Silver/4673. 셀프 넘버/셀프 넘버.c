#include <stdio.h>

int d(int n){
	int self = n;
	while (n) {
		self = self + n % 10;
		n /= 10;
	}
	return self;
}

int main() 
{
	int selfnum[10100];

	for (int i = 0; i < 10000; i++)
		selfnum[d(i)] = 1;
	for (int i = 0; i < 10000; i++) {
		if (selfnum[i] != 1)
			printf("%d\n", i);
	}
	return 0;
}