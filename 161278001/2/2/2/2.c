#include<stdio.h>
#include<stdlib.h>

int main()
{
	long long int N,i,d;
	long long int W1, W2, T1, T2;
	long long int a[100000];
	printf("please enter the quantity:\n");
	scanf_s("%lld", &N);
	printf("please enter the time of each person:\n");
	for (i = 0; i < N; i++)
	{
		scanf_s("%lld", &a[i]);
	}
	for (i = 0; i < N; i++)
	{
		if (i % 3 == 0)
		{
			if (i == N - 1)
			{
				d = N - 1;
				while (d >= 0)
				{
					T1 += a[d];
					d -= 3;
				}
			}
			d = i;
			while (d > 2)
			{
				d -= 3;
				W1 += a[d];
			}
		}
		else if (i % 3 == 1)
		{
			if (i == N - 1)
			{
				d = N - 1;
				while (d >= 0)
				{
					T1 += a[d];
					d -= 3;
				}
			}
			d = i;
			while (d > 2)
			{
				d -= 3;
				W1 += a[d];
			}
		}
		else if (i % 3 == 2)
		{
			if (i == N - 1)
			{
				d = N - 1;
				while (d >= 0)
				{
					T1 += a[d];
					d -= 3;
				}
			}
			d = i;
			while (d > 2)
			{
				d -= 3;
				W1 += a[d];
			}
		}
	}


	long long int t;
	long long int w[3];
	long long int s[3];
	

	s[0] = s[1] = s[2] = 0;
	w[0] = w[1] = w[2] = 0;
	for (i = 0; i<N; i++) {
		if (s[0] <= s[1] && s[0] <= s[2])
		    t = 0;
	    else if (s[1] < s[0] && s[1] <= s[2])
		    t = 1;
	    else if (s[2] < s[0] && s[2] < s[1])
		    t = 2;
		w[t] += s[t];
		s[t] += a[i];
	}
	W2 = w[0] + w[1] + w[2];
	if (s[0] >= s[1] && s[0] >= s[2])
		T2 = s[0];
	else if (s[1] > s[0] && s[1] >= s[2])
		T2 = s[1];
	else if (s[2] > s[0] && s[2] > s[1])
		T2 = s[2];
	printf("%lld %lld\n%lld %lld\n", W1, T1, W2, T2);
	system("pause");
}