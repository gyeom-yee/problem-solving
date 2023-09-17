int main()
{
	int n, fix;
	int count = 0;

	scanf("%d", &n);
	fix = n;

	do {
		if (n > 0 && n < 10) {
			n = 10 * n + n;
			count++;
		}
		else {
			n = (n / 10 + n % 10) % 10 + (n % 10) * 10;
			count++;
		}
		if (n == fix)
			break;
	} while (1);
	printf("%d\n", count);
	return 0;
}