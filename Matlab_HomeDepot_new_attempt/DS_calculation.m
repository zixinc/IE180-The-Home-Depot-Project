%data = readmatrix("data.csv");
load('data.mat')
data(1,:)=[];
data(:,1)=[];


[r,c]=size(data);
total=[];
for i = 1:r
    i
    %Ax<=b
    b=[data(i,8),data(i,9),data(i,10)];
    A=[data(i,15),data(i,16),data(i,17)];

    %swap dimensions and compare utility
    solution1 = slotplan1(A,b);
    solution2 = slotplan2(A,b);
    solution3 = slotplan3(A,b);
    solution4 = slotplan4(A,b);
    solution5 = slotplan5(A,b);
    solution6 = slotplan6(A,b);
    
    total1=solution1(4);
    total2=solution2(4);
    total3=solution3(4);
    total4=solution4(4);
    total5=solution5(4);
    total6=solution6(4);

    total=[total,max([total1,total2,total3,total4,total5,total5])];
end
save('total.mat','total')