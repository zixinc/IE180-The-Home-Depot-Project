%User interface to gather inputs
prompt = {'Slot width:','Slot length:','Slot height','SKU width','SKU length','SKU height'};
dlgtitle = 'Input';
dims = [1 35];
definput = {'48','144','192','16','16','2'};
user_input = inputdlg(prompt,dlgtitle,dims,definput);


%Convert input to float
array=zeros(1,length(user_input));
for i =1:length(user_input)
    array(1,i)=str2double(cell2mat(user_input(i)));
end
%nonlinear programming 
%Ax<=b
b=array(1:3);
A=array(4:6);

%swap dimensions and compare utility
solution1 = slotplan1(A,b);
solution2 = slotplan2(A,b);
solution3 = slotplan3(A,b);
solution4 = slotplan4(A,b);
solution5 = slotplan5(A,b);
solution6 = slotplan6(A,b);

total1=solution1(4)
total2=solution2(4)
total3=solution3(4)
total4=solution4(4)
total5=solution5(4)
total6=solution6(4)


