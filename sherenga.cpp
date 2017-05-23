//The problem is from http://informatics.mccme.ru/mod/statements/view3.php?id=208&chapterid=1456
#include <iostream>
#include <cmath>
using namespace std;
int main () {
	int i,n,j,k;
	cin >> n;
	int a[102];
	for (i=1;i<=n;i++) {
		cin >> a[i];
	}	
	int Petya;
	cin >> Petya;
	for (i=1;i<=n;i++){
		if (a[i] < Petya){
			cout << i;
			break;
		}
		if (Petya <= a[n]) {
			cout << n+1;
			break;	
		}
		
	}
return 0;
}
