//最近点对问题  分治法&暴力法
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <stdlib.h>

using namespace std;


typedef struct point{
    int x;
    int y;
}Point;

bool sortFunc_y(Point &,Point &);
bool sortFunc_x(Point &,Point &);
double distance(Point &, Point &);
double minLength(vector<Point>,int,int);
double violentMinLength(vector<Point> points);



int main(){
    vector<Point> points;
    for(int i=0;i<10;i++){
        auto p = Point();
        p.x = i*3+2;
        p.y = i*i*i+6;
        points.push_back(p);
        cout<<"x: "<<p.x<<" y: "<<p.y<<endl;
    }

    //首先按照x坐标排序
    sort(points.begin(),points.end(),sortFunc_x);
    cout<<"分治法： "<<minLength(points, 0, points.size()-1)<<endl;
    cout<<"暴力法： "<<violentMinLength(points)<<endl;
    return 0;
}

bool sortFunc_x(Point &a, Point &b){
    return a.x<=b.x;
}

bool sortFunc_y(Point &a, Point &b){
    return a.y <= b.y;
}
double distance(Point &a, Point &b){
    return sqrt(pow(a.x-b.x,2)+pow(a.y-b.y,2));
}

//分治法
double minLength(vector<Point> points, int begin, int end){
    if(begin+1==end){
        return distance(points[begin], points[end]);
    }
    if(begin+2==end){
        auto d1 = distance(points[begin], points[end]);
        auto d2 = distance(points[begin], points[begin+1]);
        auto d3 = distance(points[begin+1],points[end]);
        return (d1<(d2<d3?d2:d3)) ? d1: (d2<d3?d2:d3);
    }

    int mid = (begin+end)/2;

    auto left_min = minLength(points, begin, mid);
    auto right_min = minLength(points, mid+1, end);

    auto temp_min = min(left_min, right_min);
    vector<Point> p;
    for(int i=mid;(i>=begin)&&(points[mid].x-points[i].x<temp_min);i--){
        p.push_back(points[i]);
    }
    for(int i=mid+1;(i<=end)&&(points[i].x-points[mid].x<temp_min);i++){
        p.push_back(points[i]);
    }
    //按照y坐标升序
    sort(p.begin(),p.end(),sortFunc_y);
    for(int i=0;i<p.size();i++){
        for(int j=i+1;j<p.size();j++){
            if(points[j].y-points[i].y>=temp_min){
                break;
            }
            auto d = distance(points[j],points[i]);
            temp_min = temp_min<d?temp_min:d;
        }
    }
    return temp_min;
}

//暴力法
double violentMinLength(vector<Point> points){
    auto temp_min=distance(points[0],points[1]);
    for(int i=0;i<points.size();i++){
        for(int j=i+1;j<points.size();j++){
            auto temp = distance(points[i],points[j]);
            temp_min = temp_min<temp?temp_min:temp;
        }
    }
    return temp_min;
}