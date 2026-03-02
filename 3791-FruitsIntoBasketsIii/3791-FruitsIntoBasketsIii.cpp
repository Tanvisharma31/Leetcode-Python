// Last updated: 02/03/2026, 13:56:09
struct seg
{
    int n;
    vector<int> tr;

    seg(vector<int> &v)
    {
        n = 1 << (32 - __builtin_clz(max<int>(1, v.size()-1)));
        tr.resize(2*n, INT32_MIN);
        for (int i = 0; i < v.size(); i++) tr[i+n] = v[i];
        for (int i = n-1; i; i--) tr[i] = max(tr[i*2], tr[i*2+1]);
    }

    bool find(int x)
    {
        if (tr[1] < x) return false;

        int k = 1;
        while (k < n) k = tr[k*2] >= x ? k*2 : k*2+1;

        tr[k] = 0;
        while (k >>= 1) tr[k] = max(tr[k*2], tr[k*2+1]);

        return true;
    }
};

class Solution {
public:
    int numOfUnplacedFruits(vector<int>& q, vector<int>& v) 
    {
        seg tr(v);
        int cnt = 0;
        for (int x : q) if (!tr.find(x)) cnt++;
        return cnt;
    }
};