#include <bits/stdc++.h>
using namespace std;
int a[100];
int b[100];
signed main(){
    for(int i = 1;i<=28;i++){
       a[i] = i*i%29;
   }
   for(int i = 1;i<=28;i++){
    bool flag = false ;
    for(int j = 1;j<=28;j++){
      if(i == a[j]){ 
      flag = true;
      break;
     }
    }
    if(!flag) cout << i <<" ";
   }
}