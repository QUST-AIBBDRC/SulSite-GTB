clear all
clc
input=importdata('data_test.txt');
num=numel(input);
for i=1:num/2
    sequence{i}=input{2*i};
end
inputout=sequence;
out=[];
for i=1:numel(sequence)
    protein=inputout{i};
    output1 =Dipeptide(protein);%Call the Dipeptide function to calculate the cksaap value of each sequence
    out=[out;output1];
end
save test_DC.mat out