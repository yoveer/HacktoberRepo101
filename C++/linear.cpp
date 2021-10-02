//Linear Search program

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int n;
	cin>>n;
	int a[n];
	int flag=0;
	for(int i=0;i<n;i++)
	{
	    cin>>a[i];
	}
	cout<<"Enter element to be searched."<<"\n";
	int x;
	cin>>x;
	for(int i=0;i<n;i++)
	{
		if(a[i]==x)
		{
			flag=1;
			break;
		}
	}
	if(flag==1)
	{
	    cout<<"The element is found";
	}
	else
	cout<<"Not found";
	return 0;
}
