#include<iostream>

#include<conio.h>

#include<string.h>

using namespace std;

int corr(char a[50],char b[50])

{

int i,j,n,m,max;

int c=0,c1=0,c2=0,c3=0;

 n=strlen(a);

 m=strlen(b);

 cout<<endl;

 int x[10][10];

 

 if (n==0)

 cout<<m;

 else if (m==0)

 cout<<n;

 else 

 { 

      for(i=0;i<n;i++)

       {

              for(j=0;j<m;j++)

               {

                  

                    x[0][j]=0;

                    

                    

                    x[i][0]=0;

                    

                    if (a[i]==b[j])

                     { c=x[i-1][j-1]+1;

                       x[i][j]=c;

                      }

                    else

                     {c1=x[i-1][j]-1;

                      c2=x[i][j-1]-1;

                      c3=x[i-1][j-1];

                        if(c1>=c2)

                         {if (c1>c3)

                          x[i][j]=c1;

                          else 

                          x[i][j]=c3;

                         }

                       else

                        {if (c2>c3)

                         x[i][j]=c2;

                         else

                         x[i][j]=c3;

                         }

                      }

                      }

                    }

                    } 

               max=x[0][0];

               for(i=0;i<=n-1;i++)

               {

               for(j=0;j<=m-1;j++)

               {

                              if(x[i][j]>max)

                              {

                              max=x[i][j];

                              }

                              }

                              }
}

 int main()

 {

        cout<<"welcome to spell corrector";

        cout<<"enter string";

        char d;

          char a[50],b[50],c[50];

        

        cout<<"enter ";

        gets(a);

        int large=0;

        strcpy(b," nokia");

        int y;

        y=corr(a," nokia");

        large=y;

        y=corr(a," samsung");

        if (y>large)

        {strcpy(b," samsung");

        large=y;}

        y=corr(a," blackberry");

        if (y>large)

        {strcpy(b," blackberry");

         large=y;}

        y=corr(a," htc");

        if (y>large)

        {strcpy(b," htc");

        large=y;}

        y=corr(a," vertu");

        if (y>large)

        {strcpy(b," vertu");

        large=y;}

        y=corr(a," alcatel");

        if (y>large)

        {strcpy(b," alcatel");

        large=y;}

        y=corr(a," apple");

        if (y>large)

        {strcpy(b," apple");

        large=y;}

        y=corr(a," lg");

        if (y>large)

        {strcpy(b," lg");

        large=y;}

        y=corr(a," sony");

        if (y>large)

        {strcpy(b," sony");

        large=y;}

        y=corr(a," motorola");

        if (y>large)

        {strcpy(b," motorola");

        large=y;}

        y=corr(a," lava");

        if (y>large)

        {strcpy(b," lava");

        large=y;}

        y=corr(a," dell");

        if (y>large)

        {strcpy(b," dell");

        large=y;}

        y=corr(a," google");

        if (y>large)

        {strcpy(b," google");

        large=y;}

                cout<<"according to the smart spell check!!!"<<endl<<"i think u meant   : "<<b;

        getch();

        return 0;}
