#include <bits/stdc++.h>
using namespace std;

int maximizePerfectSlots(vector<int> inventory) {
    int n = inventory.size();
    vector<int> dp(n, 0);
    int ans = 0;
    
    for (int i = 0; i < n; i++) {
        int v = inventory[i];
        int key_i = i - v;   // key = (0-based index) - value
        
        // Can't form a perfect slot here (not enough prior elements)
        if (key_i < -1) continue;
        
        dp[i] = 1; // this element alone as a perfect slot
        
        for (int j = 0; j < i; j++) {
            if (dp[j] == 0) continue;
            
            int vj = inventory[j];
            int key_j = j - vj;
            
            // vj < v: j's perfect position is before i's position
            // key_j <= key_i: enough filler elements between j and i
            if (vj < v && key_j <= key_i) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        ans = max(ans, dp[i]);
    }
    
    return ans;
}
