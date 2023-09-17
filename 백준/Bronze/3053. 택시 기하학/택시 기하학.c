#include <stdio.h>
#define pi 3.14159265359

int main() {
	double r;
	scanf("%lf", &r);
	printf("%lf\n%lf\n", r * r * pi, 2 * r * r);
	return 0;
}