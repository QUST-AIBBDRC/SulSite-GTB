function [N]=ertaimatrix_N_2(data)
[a,b]=size(data);
sim_number=data;
k=unidrnd(a,1031,1);%产生一个数值在1-a之间的1031*1的矩阵
[M ID]=sort(k);%generate random numbers
sim_number1=sim_number(M,:);
Ak=ones(21,21);
for j=1:b
    xj=sim_number1(:,j);
    for i=1:21
        Ak(i,j)=numel(find(xj==i));
    end
 N=Ak/1031;
end
 
 