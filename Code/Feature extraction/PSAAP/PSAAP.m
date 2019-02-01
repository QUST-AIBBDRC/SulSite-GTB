clear all
clc
A=importdata('data_test_p.txt');
B=importdata('data_test_N.txt');
[P]=zeros(21,21);
[P]=PSAAP_P1(A);
[N,S_std]=PSAAP_N1(B);
 S=(P-N)./S_std;
 C=[A;B];
for i=2:2:numel(C)
    data1=C{i};
    data{i/2,1}=data1;
end
set=[];
for i=1:numel(data);
[set{i,1}] =ertaimatrix_1(data{i});
end
sim_number_p=cell2mat(set);
[a,b]=size(sim_number_p);
for i=1:a
    for j=1:b
        vector(i,j)=S(sim_number_p(i,j),j);
    end
end
vector(:,11)=[];
save psaap_test.mat vector



 
