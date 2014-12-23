//waterman algorithm
#include<iostream>
#include<conio.h>
#include<string>
using namespace std;
int corr(char a[50],char b[50])
{
    int i,j,n,m,max;
    int c=0,c1=0,c2=0,c3=0;

    cout<<endl;
    int x[10][10];
    n=strlen(a);
    m=strlen(b);
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
                puts(b);
                 for(i=0;i<n;i++)
                         {
                          for(j=0;j<m;j++)
                          cout<<x[i][j];
                          cout<<endl;
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
          cout<<max;
              return max;
              }
 int main()
 {
        cout<<"welcome to spell corrector";
        cout<<"enter string";
        char a[50],b[50],c[50],d[50];
        cout<<"enter ";
        int j;
        cin>>d;
        a[0]=' ';
        for(j=0;j<=strlen(a);j++)
            {a[j+1]=d[j];
            }
        int large=0;
        strcpy(b," add this to dictionary");
        int y,i;
        y=corr(a,b);
        large=y;
        char* s[]={"hp","samsung","dell","apple","nokia","htc","micromax","lava","lg","sony","karbonn","motorola"};
         for(i=0;i<12;i++)
          {
          strcpy(c,s[i]);
          y = corr(a,c);
          if(y>large)
          {
          strcpy(b,c);
          large =y;
          }
          }
        cout<<"according to the speel corrector v1.o!!!"<<endl<<"corrected word is  "<<b;
        getch();
        return 0;
 }
        
        
        
                                  
