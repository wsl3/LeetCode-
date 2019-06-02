// 0/1背包求最大价值 动态规划

#include<iostream>
using namespace std;

int maxValue(int[], int[], int, int);

int main(){
    int values[] = {8,10,6,3,7,2};
    int weight[] = {4,6,2,2,5,1};
    int count=6, bag_size=12;

    cout<<maxValue(weight,values,count,bag_size);

    return 0;
}

int maxValue(int weight[], int values[], int count, int bag_size){
    int row = count+1;
    int clo = bag_size+1;
    vector<vector<int>> max_value(row, vector<int>(clo));

    for(int i=0;i<row;i++){
        max_value[i][0] = 0;
    }
    for(int j=0;j<clo;j++){
        max_value[0][j] = 0;
    }

    for(int i=1;i<row;i++){
        for(int j=1;j<clo;j++){
            //当前物品不能放进背包
            if(weight[i-1]>j){
                max_value[i][j] = max_value[i-1][j];
            }else{
                //可方可不放
                max_value[i][j] = max(max_value[i-1][j], max_value[i-1][j-weight[i-1]]+values[i-1]);
            }
        }
    }

    return max_value[row-1][clo-1];
}
