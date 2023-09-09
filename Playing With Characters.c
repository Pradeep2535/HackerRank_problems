#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char ch,k[100],j[100];
    scanf("%c",&ch);
    scanf("\n%s",k);
    scanf("\n%[^\n]%*c",j);
    
    
    printf("%c\n%s\n%s",ch,k,j);
    

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
