//https://zerojudge.tw/ShowProblem?problemid=e287
#include<stdio.h>
int main(){
    int n,m;
    scanf("%d%d",&n,&m);
    int arr[n][m];
    int count = 0;
    // input
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            int w;
            scanf("%d",&w);
            arr[i][j] = w;
        }
    }
    //search min value
    int now_i,now_j;
    int min = 1000000;
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            if (arr[i][j]<min){
                min = arr[i][j];
                now_i = i;
                now_j = j;
            }
        }
    }

    int a,b;
    int net_i = 0,net_j = 0;

while(1){
    count+=arr[now_i][now_j];
    arr[now_i][now_j] = -1;//走過的設為-1    
    min = 10000000;
    //lift
    a = now_i,b = now_j-1;
    if (b>=0 && arr[a][b]<min && arr[a][b]!=-1){//b要>0且要小於最小值且不能=-1
        net_i = a;//假設下一個
        net_j = b;  
        min = arr[a][b];//假設最小值是往左
    }
    //right
    a = now_i, b = now_j+1;
    if (b<m && arr[a][b]<min && arr[a][b]!=-1){
        net_i = a;
        net_j = b;
        min = arr[a][b];
    }
    //up
    a = now_i-1,b = now_j;
    if (a>=0 && arr[a][b]<min && arr[a][b]!=-1){
        net_i = a;
        net_j = b;
        min = arr[a][b];
    }
    //down
    a = now_i+1,b = now_j;
    if (a<n && arr[a][b]<min && arr[a][b]!=-1){
        net_i = a;
        net_j = b;
        min = arr[a][b];
    }

    if (min == 10000000){
        break;
    }
    if (arr[net_i][net_j] == -1){
        break;
    }
    now_i = net_i;
    now_j = net_j;

    }
    printf("%d\n",count);


    return 0;
}
