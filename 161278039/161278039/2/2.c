#include <stdio.h>

int main(){
	int n,a[100000],i,min,max;
	int q[3]={0},sum[3]={0},wait[3]={0};
	int qq[3]={0},j,ww[3]={0},t;
	scanf("%d",&n);
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	
	for(i=0;i<n;i++){
		min=0;
		if(q[min]>q[1]) min=1;
		if(q[min]>q[2]) min=2;
		q[min]++;
		wait[min]+=sum[min];
		sum[min]+=a[i];
	}
	max=0;
	if(sum[max]<sum[1]) max=1;
	if(sum[max]<sum[2]) max=2;
	
	for(i=0;i<n;i++){
		min=0;
		if(qq[min]>qq[1]) min=1;
		if(qq[min]>qq[2]) min=2;
		ww[min]+=qq[min];
		qq[min]+=a[i];
	}
	j=0;
	if(ww[j]<ww[1]) j=1;
	if(ww[j]<ww[2]) j=2;
	t=0;
	if(qq[t]<qq[1]) t=1;
	if(qq[t]<qq[2]) t=2;
	printf("W1:%d T1:%d\n",wait[0]+wait[1]+wait[2],sum[max]);
	printf("W2:%d T2:%d\n",ww[j],qq[t]);
	return 0;
} 
