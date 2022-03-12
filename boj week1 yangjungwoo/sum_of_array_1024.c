#include <iostream>

using namespace std;
int main(){

    long int n;
    int L;
    cin>>n>>L;

    long int s = -1; //수열중 가장 작은수
    long int e = -1;// 수열중 가장 큰 수 
    for(long int i = L ; i <= 100 ; i++){
        // i가 홀수일 때     /L이 L~100까지 반복
            if(n%i == 0){  // n=18 i=3   6 6 6     
                s = n/i - i/2;   //s = 18/3 - 3/2  =5
                e = n/i + i/2;   //e = 18/3 + 3/2  =7
                break;
            }
        }
        // i가 짝수일 때
        else{  // 18 4 
            if(n%i == i/2){      //18%4 == 4/2
                s = n/i - i/2 +1;  //4 -1+1   ==4
                e = n/i + i/2;//  4+2==6 
                break;
            }
        }
    }
    if(s < 0){
        cout<<-1<<endl;
    }
    else{
        for(long int i = s ; i<= e; i++){
            cout<< i <<" ";
        } 
        cout<<endl;
    }




    return 0;
}