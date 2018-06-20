#include<stdio.h>

int main()
{
	int N, P,i,s;
	int a[1000];
	int b[1000];
	printf("please enter the number of restuants:\n");
	scanf_s("%d", &N);
	printf("please enter the number of warehouse:\n");
	scanf_s("%d", &P);
	printf("enter the locations:");
	for (i = 0; i < N; i++)
	{
		scanf_s("%d", &a[i]);
	}
	if (P > N)
		printf("ÊäÈë´íÎó\n");
	else if (P == N)
	{
		for (i = 0; i < N; i++)
		{
			printf("%d", a[i]);
		}
	}
	else if (P < N)
	{

	}
}