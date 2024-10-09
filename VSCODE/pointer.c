#include<stdio.h>

int main ()
{
    
    int a[10]={1,3,4,5,6,7,8,9,0,2};
    int flag=0;
    int x;

    printf("enter the number to find:");
    scanf("%d",&x);
    for (int i=0;i<10;i++)
    {
        if((a[i]) == x)
        {
            flag = 1;
            break; 
        }
    }
    if(flag == 0)
    {
        printf("Not Found!");
    }
    else
    {
        printf("found it!");
    }
}