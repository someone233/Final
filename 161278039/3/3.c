#include <stdio.h>

int main(){
	int n,m,i,d,j=0,k=0,buy=0,sell=0;
	int tb[100],ts[100];
	int tc[100],c[100],p,t,temp1;
	float sum1=0,sum2=0,b[100],s[100],temp2;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&temp1);
		scanf("%f",&temp2);
		scanf("%d",&d);
		if(d==1){
			tb[buy]=temp1;
			b[buy++]=temp2;
		}
		else{
			ts[sell]=temp1;
			s[sell++]=temp2;
		}
	}
	
	scanf("%d",&m);
	for(i=0;i<m;i++){
		scanf("%d",&tc[j]);
		scanf("%d",&c[j++]);
	}
	
	for(i=0;i<buy;i++){
		for(j=0;j<m&&tc[j]<tb[i];j++);
		p=c[j-1];
		if(p*b[i]*0.2<5) t=5;
		else t=p*b[i]*0.2;
		sum1+=p*b[i]*100+t+b[i]/10+1;	
	}
	
	for(i=0;i<sell;i++){
		for(j=0;j<m&&tc[j]<ts[i];j++);
		p=c[j-1];
		if(p*s[i]*0.2<5) t=5;
		else t=p*s[i]*0.2;
		sum2+=p*s[i]*100*0.999-t-s[i]/10-1;	
	}	
	printf("%.2f",sum2-sum1);
	return 0;
	
} 
