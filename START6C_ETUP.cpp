#include <iostream>
using namespace std;


long long factorial_dp(long num)
{
    long long factorial[100001], res;
    
    factorial[0] = 1;
    factorial[1] = 1;
    
    for(long i=2; i<=num; ++i)
    {
        factorial[i] = i * factorial[i-1];
        //cout << factorial[i] << endl;
    }
    
    return factorial[num];
}

/*
long long factorial_dp(long num)
{
    if (num == 0)
        return 1;
        
    else if (num == 1)
        return 1;

    else 
        return num * factorial_dp(num-1);
    
}
*/
int main()
{
    long t, n, q, A[100001], l, r, i, j, k, even, odd, count;
    //long long result; 
    long long first, second;
    
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
        
        /* debug start
        for(i=0; i <= n; ++i)
            cout << A[i] << " ";
        cout << endl;
        
        debug end */
        
        for(j=0; j < q; ++j)
        {
            
            cin >> l >> r;
            // debug start
            //cout << "Here" << endl;

            even = A[r] - A[l-1];
            odd = (r-l+1) - even;
            
            //cout << even << " " << odd << endl;
            
            if (even < 3)
                first = 0;
            else 
                first = factorial_dp(even) / (6 * factorial_dp(even-3));
            
            if (odd < 2)
                second = 0;
            else
                second = (factorial_dp(odd) * even) / (2*factorial_dp(odd-2));
            // debug end            
            //result = (factorial_dp(even) / (6 * factorial_dp(even-3))) + 
            //    (factorial_dp(odd) * even) / (2*factorial_dp(odd-2)); 
            
            
            cout << first + second << endl;
            //cout << second << endl;
            
            
            //cout << result << endl;
        }
    }
    
    return 0;
}
