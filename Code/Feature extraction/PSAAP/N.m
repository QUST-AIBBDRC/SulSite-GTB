clear all
clc
A=importdata('data_test_p.txt');
B=importdata('data_test_N.txt');
[P]=zeros(21,21);
[P]=PSAAP_P1(A);
[N,S_std]=PSAAP_N1(B);
 S=(P-N)./S_std;
for i=2:2:numel(B)
    data1=B{i};
    data{i/2,1}=data1;
end
set=[];
for i=1:numel(data);
[set{i,1}] =ertaimatrix_1(data{i});
end
sim_number_N=cell2mat(set);
[Np,b]=size(sim_number_N);
for i=1:Np
    for j=1:b
        vector_p(i,j)=S(sim_number_N(i,j),j);
    end
end
vector_n=vector_p;
vector_n(:,11)=[];
save psaap_test_N.mat vector_n



 
