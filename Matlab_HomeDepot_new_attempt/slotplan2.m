function solution = slotplan2(A,b)
%rotate item to aligh item height to slot width, item width to slot height
A_new=zeros(1,3);
A_new(1)=A(2);
A_new(2)=A(1);
A_new(3)=A(3);
A=A_new;

type objfunx
x = optimvar('x');
y = optimvar('y');
z = optimvar('z');
obj = objfunx(x,y,z);
prob = optimproblem('Objective',obj);
constraint1= A(1)*x<=b(1);
constraint2= A(2)*y<=b(2);
constraint3= A(3)*z<=b(3);
constraint4= x>=0;
constraint5= y>=0;
constraint6= z>=0;
prob.Constraints.constr1 = constraint1;
prob.Constraints.constr2 = constraint2;
prob.Constraints.constr3 = constraint3;
prob.Constraints.constr4 = constraint4;
prob.Constraints.constr5 = constraint5;
prob.Constraints.constr6 = constraint6;

x0.x = 3;
x0.y = 3;
x0.z = 3;

[sol,fval] = solve(prob,x0);
x = floor(vertcat(sol.x));
y = floor(vertcat(sol.y));
z = floor(vertcat(sol.z));
total_item=x*y*z;
solution=[x,y,z,total_item]

end