function [set] =ertaimatrix_1( A )
window=21;
set=[];
for j=1:window
B=A(:,j);
chen=[];
C=B;
str=strrep(C,'A','01');
str=strrep(str,'C','02');
str=strrep(str,'D','03');
str=strrep(str,'E','04');
str=strrep(str,'F','05');
str=strrep(str,'G','06');
str=strrep(str,'H','07');
str=strrep(str,'I','08');
str=strrep(str,'K','09');
str=strrep(str,'L','10');
str=strrep(str,'M','11');
str=strrep(str,'N','12');
str=strrep(str,'P','13');
str=strrep(str,'Q','14');
str=strrep(str,'R','15');
str=strrep(str,'S','16');
str=strrep(str,'T','17');
str=strrep(str,'V','18');
str=strrep(str,'W','19');
str=strrep(str,'Y','20');
str=strrep(str,'-','21');
chen=[chen;str];
str=[];
shuju=str2num(chen);
set=[set,shuju];
end
end

