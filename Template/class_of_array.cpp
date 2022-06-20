#include<iostream>
#include<string>
using namespace std;
class student{
    public:
    string name;
    int roll;
    int marks;
};
void student_data(student data[],int n){
    for(int i=0;i<n;i++){
        cout<<"Enter deatais of "<< i<<" students:";
        cin>>data[i].name;
        cin>>data[i].roll;
        cin>>data[i].marks;
    }
}
void display_data(student data[],int n){
    for(int i=0;i<n;i++){
        cout<<"Name:"<<data[i].name<<" roll:"<<data[i].roll<<" marks:"<<data[i].marks<<endl;
    }
}
int main(){
    const int n=3;
    student data[n];
    student_data(data,n);
    display_data(data,n);
}
