#include <iostream>
using namespace std;

int main()
{
    long t, n, q, A[100001], l, r, i, j, k, even, odd, count, first, second;
    
    cin >> t;
    
    while (t--)
    {
        cin >> n >> q;
        
        A[0] = 0;
        count = 0;
        
        for(i=1; i <= n; ++i)
        {
            cin >> A[i]; 
            
            if (A[i] % 2 == 0)
            {
                ++count;
            }
            
            A[i] = count;
            
        }

        for(j=0; j < q; ++j)
        {
            
            cin >> l >> r;

            even = A[r] - A[l-1];
            odd = (r-l+1) - even;
            
            first = even*(even-1)*(even-2) / 6;
            second = odd*(odd-1)*even / 2;
            
            cout << first + second << endl;

        }
    }
    
    return 0;
}
