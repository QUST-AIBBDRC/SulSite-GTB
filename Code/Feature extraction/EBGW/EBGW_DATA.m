clear all
clc
input=importdata('data_train.txt');
data=input(2:2:end,:);
[m,n]=size(data);
vector=[];
for i=1:m;
 vector= [vector;EBGW(data{i})];
end
save EBGW_test_p.mat vector

