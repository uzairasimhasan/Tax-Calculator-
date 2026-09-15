#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<windows.h>
#include<string.h>
int main(){
    unsigned int salary,fixedamount,exceeding_amount;
    char op;
    float tax,total_salary;
    printf("Enter your salary: ");
    system("espeak -v en+f3 \"Enter your salary\"");
    scanf("%u",&salary);
    printf("Do you have the tax rate calculated or you want me to do it for you?(Y/N)\n");
    system("espeak -v en+f3 \"Do you have the tax rate calculated or you want me to do it for you?\"");
    op = getch();
    if (toupper(op)=='Y' && salary>600000){
            printf("Enter the tax amount:");
            system("espeak \"Enter the tax ammount\"");
            scanf("%f",&tax);
            printf("Enter the fixed amount: ");
            scanf("%f",&fixedamount);
            exceeding_amount = salary-600000;
            total_salary = salary-((exceeding_amount*tax)+fixedamount);
            printf("Total Salary: Rs%.2f",total_salary);
    }
    else{
        if(salary<=600000){
            printf("\nNO TAX!\n");
            printf("Total Salary: %d",salary);
        }
        else if(salary>600000 && salary<=1200000){
            exceeding_amount=salary-600000;
            tax = exceeding_amount*0.01;
            printf("\nTAX MONEY: Rs%f\n",tax);
            total_salary = salary-tax;
            printf("Total Salary: %f",total_salary);
        }
        else if(salary>1200000 && salary<=2200000){
            fixedamount=6000;
            exceeding_amount=salary-1200000;
            tax = (exceeding_amount*tax)+fixedamount;
            printf("\nTAX MONEY: %f\n",tax);
            total_salary = salary-tax;
            printf("Total Salary: %f",total_salary);
        }
        else{
            printf("We Will Decide Your Tax Later!");
        }
    }

}
