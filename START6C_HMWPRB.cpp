#include <iostream>
using namespace std;

//#define min 10000000000

int main() {
    int t, days, hacks, hw[1000001];
    
    cin >> t;
    
    for(int i=0; i < t; ++t)
    {
        cin >> days >> hacks;
        
        for(int j=0; j < days; ++j)
            cin >> hw[j];
            
        long min = 10000000000;

        int temp = 0;
        int p = 0;
        while(p < days/hacks)
        {    
            //cout << "days/hacks: " << days/hacks << endl;
            if (p >= days/hacks)
                break;
            //cout << "p: " << p << endl;
            int sum = 0;
            static int temp = 0;
            //cout << "temp: " << temp << endl;
            for(int j=temp; j < days; j+=hacks+1)
            {
                sum += hw[j];
                //cout << sum << " ";
            }
            
            ++temp;
            
            if (sum < min) 
            {
                min = sum;
                //cout << "min " << p+1 << ": " << min << endl;   
            }
            ++p;
        }
        
        cout << min << endl;
        
    }
    
    
    


	return 0;
}
