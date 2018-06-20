#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int m;
	cin >> m;
	int* t = new int[m];
	int* a = new int[m];
	int* d = new int[m];
	for (int i = 0; i < m; i++)
		cin >> t[i] >> a[i] >> d[i];
	int n;
	cin >> n;
	int* t2 = new int[n];
	int* v = new int[n];
	for (int i = 0; i < n; i++)
		cin >> t2[i] >> v[i];
	
	int buy = 0;
	int sell = 0;
	double pay = 0;
	double profit = 0;
	for (int i = 0; i < m; i++)
	{
		int price = 0;
		int j = 0;
		for (; j < n - 1; j++)
		{
			//cout << t2[j] << " " << t[i] <<" "<< t2[j + 1];
			if (t2[j] <= t[i] && t2[j+1] > t[i])
			{
				price = v[j];
				break;
			}
		}
		if (j == n - 1)
			price = v[n - 1];
		if (d[i] == 1)
		{
			buy += a[i] * 100 * price;
			double pay1 = buy * 0.002;
			if (pay1 < 5)
				pay1 = 5;
			double pay2 = int(a[i] * 100 / 1000);
			double pay3 = 1;
			pay += pay1 + pay2 + pay3;
			cout << pay << endl;
		}
		else
		{
			sell += a[i] * 100 * price;
			double pay1 = sell * 0.002;
			if (pay1 < 5)
				pay1 = 5;
			double pay2 = int(a[i] * 100 / 1000);
			double pay3 = 1;
			double pay4 = sell * 0.001;
			pay += pay1 + pay2 + pay3 + pay4;
			cout << pay << endl;
		}
	}
	profit = sell - buy - pay;
	cout << setiosflags(ios::fixed) << setprecision(2) << profit;
	system("PAUSE");
}
