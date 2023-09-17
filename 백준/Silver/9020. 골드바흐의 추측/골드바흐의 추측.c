#include <stdio.h>

int main() {
	int t, n, half;
	int a, b, i, flag_a, flag_b;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		half = n / 2;
		for (a = half; a; a--) {
			flag_a = flag_b = 0;
			for (i = 2; i * i <= a; i++) {
				if (a % i == 0) {
					flag_a = 1;
					break;
				}
			}
			if (flag_a != 1) {
				b = n - a;
				for (i = 2; i * i <= b; i++) {
					if (b % i == 0) {
						flag_b = 1;
						break;
					}
				}
				if (flag_b != 1) {
					printf("%d %d\n", a, b);
					break;
				}
			}
		}
	}
	return 0;
}