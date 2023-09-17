#include <stdio.h>
#include <math.h>

int turret(double x1, double y1, double r1, double x2, double y2, double r2) {
	double d = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
	double r_minus = r1 > r2 ? r1 - r2 : r2 - r1;
	if (d > r_minus && d < r1 + r2)
		return 2;
	else if (d == 0 && r1 == r2)
		return -1;
	else if (d == r_minus || d == r1 + r2)
		return 1;
	else
		return 0;
}

int main() {
	int t;
	double x1, y1, r1, x2, y2, r2;
	scanf("%d", &t);
	while (t--) {
		scanf("%lf %lf %lf %lf %lf %lf", &x1, &y1, &r1, &x2, &y2, &r2);
		printf("%d\n", turret(x1, y1, r1, x2, y2, r2));
	}
	return 0;
}