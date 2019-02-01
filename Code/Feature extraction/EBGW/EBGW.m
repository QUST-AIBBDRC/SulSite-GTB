function x = EBGW_yu(protein)
%protein='TFVPAKKVKDLLK';
l=length(protein);
C1={'G','A','V','L','I','M','P','F','W'};
C2={'Q','N','S','T','Y','C'};
C3={'D','E'};
C4={'H','K','R'};
P1=[C1,C2];  
P2=[C1,C3];   
P3=[C1,C4];
inp1=zeros(1,l);
inp2=zeros(1,l);
inp3=zeros(1,l);
h=[];
for i=1:l;
    for j=1:length(P1)
        if protein(i)==P1{j};
            h(j)=1;
        end
    end
    if sum(h)==1
       inp1(i)=1;    
    end
    h=[];
end
for i=1:l;
    for j=1:length(P2)
        if protein(i)==P2{j};
            h(j)=1;
        end
    end
    if sum(h)==1
       inp2(i)=1;    
    end
    h=[];
end
for i=1:l;
    for j=1:length(P3)
        if protein(i)==P3{j};
            h(j)=1;
        end
    end
    if sum(h)==1
       inp3(i)=1;    
    end
    h=[];
end
k=5;
ll=[];
x1=[];
x2=[];
x3=[];
for i=1:k;
    ll=[ll,floor(i/k*l)];
    x1=[x1,sum(inp1(1:ll(i))==1)/length(inp1(1:ll(i)))];
    x2=[x2,sum(inp2(1:ll(i))==1)/length(inp2(1:ll(i)))];
    x3=[x3,sum(inp3(1:ll(i))==1)/length(inp3(1:ll(i)))];
end
x=[x1,x2,x3];

end

