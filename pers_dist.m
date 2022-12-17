% This script computes and plot the kernel distribution that approximates
% the 0- and 1- persistence dsitribution of two groups. These are given in
% figure 2 of the paper in the case of controls and ISAD subjects.
% The script takes as input string vectors with the file names of the
% barcodes. 

group1=[];
group2=[];
s1=size(group1, 2);
s2=size(group2, 2);
persg1_0=[];
persg1_1=[];
persg2_0=[];
persg2_1=[];
set(gcf,'renderer','Painters');
for i=1:s1
    bc_g1_0=load(char(group1(i)));
    bc_g1_1=load(char(group1(i)));
    persg1_0=[persg1_0; bc_g1_0(:, 2)-bc_g1_0(:, 1)];
    persg1_1=[persg1_1; bc_g1_1(:, 2)-bc_g1_1(:, 1)];
end
for i=1:s2
    bc_g1_0=load(char(group2(i)));
    bc_g1_1=load(char(group2(i)));
    persg2_0=[persg2_0; bc_g1_0(:, 2)-bc_g1_0(:, 1)];
    persg2_1=[persg2_1; bc_g1_1(:, 2)-bc_g1_1(:, 1)];
end
%dimension 0
persg1_0(persg1_0==inf)=[];
[fc,xic] = ksdensity(persg1_0); 
plot(xic,fc);
persg2_0(persg2_0==inf)=[];
[fi,xii] = ksdensity(persg2_0); 
hold on
plot(xii,fi);
hold off
x=0:0.01:0.15;
pdc = fitdist(persg1_0,'Kernel');
pdi = fitdist(persg2_0,'Kernel');
yc=pdf(pdc, x);
yi=pdf(pdi, x);
plot(x, yc, 'b');
hold on 
plot(x, yi, 'r');
hold off
legend('group1', 'group2')
% dimension 1
persg1_1(persg1_0==inf)=[];
[fc,xic] = ksdensity(persg1_1); 
figure
plot(xic,fc);
persg2_1(persg2_1==inf)=[];
[fi,xii] = ksdensity(persg2_1); 
hold on
plot(xii,fi);
hold off
x=0:0.01:0.15;
pdc = fitdist(persg1_1,'Kernel');
pdi = fitdist(persg2_1,'Kernel');
yc=pdf(pdc, x);
yi=pdf(pdi, x);
plot(x, yc, 'b');
hold on 
plot(x, yi, 'r');
hold off
legend('group1', 'group2')