#include <stdio.h>

int powered(int x, int y)
{
	if (y == 1)
	{
		return x;
	}
	else
		return x * powered(x, y - 1);
}
int main()
{
	int x, y;
	printf("Enter a number :");
	scanf("%d%d", &x, &y);
	printf("%d", powered(x, y));

	return 0;
}