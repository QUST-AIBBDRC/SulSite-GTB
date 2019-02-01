function [N,S_std]=PSAAP_N1(A)
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
N=zeros(21,21);
 for k=1:10
N1=ertaimatrix_N_2(sim_number);
N=N+N1;
M(:,:,k)=N1;
 end
for i=1:21
    for j=1:21
        S_std(i,j)=std(M(i,j,:));
    end
end
NN=N/10;
end


