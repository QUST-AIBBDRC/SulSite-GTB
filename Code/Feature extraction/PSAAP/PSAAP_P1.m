function [M_P]=PSAAP_P1(A)
[a,b]=size(A);
for i=2:2:a
    data1=A{i};
    data{i/2,1}=data1;
end
set=[];
for i=1:numel(data);
[set{i,1}] =ertaimatrix_1(data{i});
end
sim_number=cell2mat(set);
[M_P]=ertaimatrix_2(sim_number);
end
