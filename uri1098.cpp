#include <bits/stdc++.h>
using namespace std;
#define lli long long int

int main()
{
    for(double i=0 ; i<=2; i= i+ 0.2){
        int cnt=0,incr=1;
        while(cnt<3){
            cout<<"I="<<i<<" J="<<i+incr<<"\n";
            incr++;
            cnt++;
        }

    }
}
