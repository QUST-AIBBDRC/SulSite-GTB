clear all
clc
%input1=importdata('data_train_p.txt');
%input2=importdata('data_train_N.txt');
%input=[input1;input2];
input=importdata('data_train.txt');
data=input(2:2:end,:);
[m,n]=size(data);
vector=[];
for i=1:m;
 vector= [vector;PWAAC(data{i})];
end
save PWAAC_train.mat vector

