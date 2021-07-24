#include <iostream>
using namespace std;

int main()
{
    int t, A[100001];
    
    cin >> t;
    
    while(t--)
    {
        int n, q;
        
        cin >> n >> q;
        
        int j=0;
        for(; j < n; ++j)
        {
            cin >> A[j];    
        }
        
        int k=0;    
        for(; k < q; ++k)
        {
            int a, b;
            cin >> a >> b;
            
            int count = 0;
            
            int p=a-1;
            for(; p < b; ++p)
            {
                int q=p+1;
                for(; q < b; ++q)
                {
                    int r=q+1;
                    for(; r<b; ++r)

                        if (!((A[p] + A[q] + A[r]) & 1))
                            ++count;
            
                }        
            }
            cout << count << endl;
    
        }        
    }
    return 0;
}
