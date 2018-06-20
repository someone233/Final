#include<stdio.h>
#include<stdlib.h>

int main()
{
	int a, b, c;
	printf("please enter two integers:\n");
	scanf_s("%d%d", &a, &b);
	c = a * b;
	int a1, b1, c1;
	c1 = c; b1 = b; a1 = a;
	int i = 0;
	while (c1 > 0)
	{
		c1 = c1 / 10;
		i++;
	}
	int j = 0;
	while (a1 > 0)
	{
		a1 = a1 / 10;
		j++;
	}
	int k = 0;
	while (b1 > 0)
	{
		b1 = b1 / 10;
		k++;
	}
	int x1, x2;
	x1 = i - j;
	x2 = i - k;
	int q = 0;
	int w, e;
	if (k > j)
	{
		w = a; a = b; b = w;
		e = j; j = k; k = e;
	}
	for (q = 0; q < x1; q++)
	{
		printf(" ");
	}
	printf("%d\n", a);
	for (q = 0; q < x2; q++)
	{
		printf(" ");
	}
	printf("%d\n", b);
	for (q = 0; q < i; q++)
	{
		printf("-");
	}
	printf("\n%d\n", c);
	system("pause");
}
