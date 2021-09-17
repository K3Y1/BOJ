#include <iostream>

int tens(int k)
{
    if(k==0) return 10;
    int i=0;
    int ten = 1;
    while(ten > k)
    {
        ten = ten * 10; i++;
    }
    return ten;
}

int main()
{
    int K, N;
    std::cin >> K >> N;
    int i = 1; int j = 1; int a[K+1] ; int temp;
    for (; i <= K; i++)
    {
        std::cin >> a[i];
    }
    for (i = 1; i <= K; i++) // a[1] > a[2] > ...
    {
        for (j = 2; j <= K; j++)
        {
            if (a[j - 1] < a[j])
            {
                temp = a[j - 1]; a[j - 1] = a[j]; a[j] = temp;
            }
        }
    }
    int biggest = a[1];
    for (i = 1; i <= K; i++) // i < j ; a[i] = 9, a[j] = 98 b/c 998 > 989
    {
        for (j = 2; j <= K; j++)
        {
            if (a[j-1] * tens(a[j]) + a[j] < a[j] * tens(a[j-1]) + a[j-1] )
            {
                temp = a[j - 1]; a[j - 1] = a[j]; a[j] = temp;
            }
        }
    }
    for(i=1; i<=K; i++)
    {
        if(a[i] == biggest)
        {
            for(j=1; j<=N-K+1; j++)
            {
                std::cout << a[i];
            }
        }
        else
        { std::cout << a[i]; }
    }
}
