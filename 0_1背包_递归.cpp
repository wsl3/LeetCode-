// 0/1背包求最大价值 递归

#include<iostream>
using namespace std;

int maxValue(int[], int[], int, int);

int main(){
    int values[] = {8,10,6,3,7,2};
    int weight[] = {4,6,2,2,5,1};
    int count=6, bag_size=12;

    cout<<maxValue(weight,values,count-1,bag_size);

    return 0;
}

int maxValue(int weight[], int values[], int index, int leftWeight){
    if(index<0 || leftWeight <=0){
        return 0;
    }
    //不能放
    if(leftWeight<weight[index]){
        return maxValue(weight, values, index-1, leftWeight);
    }
    //可放可不放, 求两者最大值
    auto not_add_this = maxValue(weight, values, index-1, leftWeight);
    auto add_this = maxValue(weight, values, index-1,leftWeight-weight[index])+values[index];

    return max(not_add_this, add_this);
}