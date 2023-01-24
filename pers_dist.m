% This script computes probability distributions, using kernel density 
% estimation, that approximate the probability distributions of the random
% variables whose values are the persistence of all the generators of H_0 and
% H_1 grouped in control and ISAD subjects.
% Also plots the obtained probabilty density functions given in Figure 2 of the paper.
% To run this script, the barcodes need to be in the same folder as this script 

controls=["01_g4s01",  "02_g4s05",  "03_g4s11",  "04_g5s01",  "05_g5s02",  "06_g5s06",  "07_g5s08",  "08_g5s10",...
    "09_g5s12",  "10_g5s13",  "11_g6s01",  "12_g6s04",  "13_g6s06",  "14_g6s08",...
    "15_g6s09",  "16_g6s13",  "17_g6s14",  "18_g7c01",  "19_g7c04"];
ISAD=["20_g7s01",  "21_g7s02",  "22_g7s03",  "23_g7s05",  "24_g7s06",  "25_g7s08",  "26_g7s09",...
    "27_g7s10",  "28_g7s11",  "29_g7s12",  "30_g7s13",  "32_g7s16",  "33_g7s17",  "34_g7s18",  "35_g7s19",...
    "36_g7s22",  "37_g7s23",  "38_g7s24",  "39_g7s25",  "40_g7s26",  "41_g7s28",  "42_g7s29",  "43_g7s30"];
s1=size(controls, 2);
s2=size(ISAD, 2);
persc_0=[];
persc_1=[];
persi_0=[];
persi_1=[];
set(gcf,'renderer','Painters');
for i=1:s1
    bc_c_0=load([char(controls(i)), '_bc_0.txt']);
    bc_c_1=load([char(controls(i)), '_bc_1.txt']);
    persc_0=[persc_0; bc_c_0(:, 2)-bc_c_0(:, 1)];
    persc_1=[persc_1; bc_c_1(:, 2)-bc_c_1(:, 1)];
end
for i=1:s2
    bc_i_0=load([char(ISAD(i)), '_bc_0.txt']);
    bc_i_1=load([char(ISAD(i)), '_bc_1.txt']);
    persi_0=[persi_0; bc_i_0(:, 2)-bc_i_0(:, 1)];
    persi_1=[persi_1; bc_i_1(:, 2)-bc_i_1(:, 1)];
end
%dimension 0
persc_0(persc_0==inf)=[];
persi_0(persi_0==inf)=[];
x=0:0.01:0.15;
pdc = fitdist(persc_0,'Kernel');
pdi = fitdist(persi_0,'Kernel');
yc=pdf(pdc, x);
yi=pdf(pdi, x);
plot(x, yc, 'b');
hold on 
plot(x, yi, 'r');
hold off
legend('controls', 'ISAD')
% dimension 1
persc_1(persc_0==inf)=[];
figure
persi_1(persi_1==inf)=[];
x=0:0.01:0.15;
pdc = fitdist(persc_1,'Kernel');
pdi = fitdist(persi_1,'Kernel');
yc=pdf(pdc, x);
yi=pdf(pdi, x);
plot(x, yc, 'b');
hold on 
plot(x, yi, 'r');
hold off
legend('controls', 'ISAD')
