#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MAX = 2e9;
typedef pair<int, int> pi;
int k, x, y;
int dp[256][256];// 타일이 칠해진 배열
int clk = 0;// 칠할 타일의 넘버
bool isin(int x, int y, int siz) {//정해진 구간에서 칠해진(혹은 뚫린)타일이 있으면  0을 리턴
    for (int i = x; i < x + siz; i++) {
        for (int j = y; j < y + siz; j++) {
            if (dp[i][j] != 0)return 0;
        }
    }
    return 1;
}
void rec(int x, int y, int siz) {
        ++clk;
        // 4구간으로 나눈뒤에 이 구간내에 칠해진 타일이 없는경우(즉, 아직 불완전타일)이 아니면, 그 부분들의 가운데를 칠해준다.
        if (isin(x, y, siz >> 1))dp[x + (siz >> 1) - 1][y + (siz >> 1) - 1] = clk;
        if (isin(x, y + (siz >> 1), siz >> 1))dp[x + (siz >> 1) - 1][y + (siz >> 1)] = clk;
        if (isin(x + (siz >> 1), y, siz >> 1))dp[x + (siz >> 1)][y + (siz >> 1) - 1] = clk;
        if (isin(x + (siz >> 1), y + (siz >> 1), siz >> 1))dp[x + (siz >> 1)][y + (siz >> 1)] = clk;
        // 재귀적으로 이 과정을 반복한다.    
        if (siz == 2)return;
    
        rec(x, y, siz >> 1);
        rec(x + (siz >> 1), y, siz >> 1);
        rec(x, y + (siz >> 1), siz >> 1);
        rec(x + (siz >> 1), y + (siz >> 1), siz >> 1);
}
int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> k >> x >> y;
    dp[y - 1][x - 1] = -1;
    rec(0, 0, 1 << k);
    for (int i = (1 << k) - 1; i >= 0; i--) {
        for (int j = 0; j < (1 << k); j++) {
            cout << dp[i][j] << " ";
        }
        cout << "\n";
    }
}