%% Demo for structure-oriented filtering algorithm of 2D data
%
%  The input free parameters of the slope estimation and structural
%  filtering are listed as follows: 
%-------------------------------------------------------------------------
%  1. slope estimation (str_dip2d.m)
%  din: input data for slope estimation
%  niter: number of non-linear iterations (default value 5-10)
%  liter: number of linear iterations (default value 10-20)
%  order: accuracy order of PWD filter (default value 1 or 2)
%  eps_dv: regualrization parameter in the non-linear iteration (default value 0.01)
%  eps_cg: regualrization parameter in the linear iteration (CG) (default value 1)
%  eps_cg: tolerance in the linear iteration (CG) (default value 0.000001)
%  rect:  size of the triangle smoothing operator (default value 5-10)
%  verb: verbosity flag that controls if printing the iteration number of CG (default value 1)
%-------------------------------------------------------------------------
%  2. structural filtering (str_pwsmooth_lop2d.m)
%  dn: noisy data
%  dip: slope field
%  ns: spray radius (smoothing length) (default value 1-4)
%  order: accuracy order of PWD filter (default value 1 or 2)
%  eps: regularization parameter (default value 0.01);
%
% Copyright (c) 2021 by the Society of Exploration Geophysicists.
% You must read and accept usage terms at:
%    https://software.seg.org/disclaimer.txt before use.

%% Generate synthetic data
clear;clc;close all;

% w=str_ricker(30,0.001,0.1);
% t=zeros(300,1000);
% sigma=300;A=100;B=200;
% for i=1:size(t,2)
% k=floor(-A*exp(-(i-size(t,2)/2).^2/sigma.^2)+B);
% if k>0&&k<=size(t,1)
%     t(k,i)=1;
% end
% end
% for i=1:size(t,2)
% data(:,i)=conv(t(:,i),w);
% end
% data=data(:,1:10:end);
% data=data./max(max(data));

% read legacy_originalTrace.dat into data and transpose
% data = load('legacy_originalTrace_SLMO.dat');
% data = load('legacy_originalTrace_DAT0003.dat');
% data = load('legacy_originalTrace_ladder.dat');
% data = load('legacy_originalTrace_SLMO_ROUGH.dat');
% data = load('legacy_originalTrace_SLOL.dat');
% data = load("legacy_originalTrace_SLOL_NL.dat");
% data = load('legacy_originalTrace_SLOLLarge_NL.dat');
% data = load('legacy_originalTrace_ladderLargeAC.dat');
data = load('QLDA_AC.dat');
% data = data';

scnoi=(rand(size(data))*2-1)*0.2;
% dn=data+scnoi;
dn = data;


% plot figures
lim1=-1;lim2=1;
x1=100;y1=100;dx=400;dy=500;

figure;imagesc(data);ax = gca;

set(ax, 'CLim', [lim1 lim2]);
set(gcf,'position',[x1,y1,dx,dy]);
colorbar;xlabel('Trace','FontName','Arial','FontWeight','Bold','FontSize',14);
ylabel('Time (ms)','FontName','Arial','FontWeight','Bold','FontSize',14);
set(gca,'FontName','Arial','FontSize',14,'LineWidth',1);
title('clean data');

figure;imagesc(dn);ax = gca;

set(ax, 'CLim', [lim1 lim2]);
set(gcf,'position',[x1,y1,dx,dy]);
colorbar;xlabel('Trace','FontName','Arial','FontWeight','Bold','FontSize',14);
ylabel('Time (ms)','FontName','Arial','FontWeight','Bold','FontSize',14);
set(gca,'FontName','Arial','FontSize',14,'LineWidth',1);
title('noisy data');

%% Slope estimation
dtemp=dn*0;%dtemp is the preprocessed data
for i=1:size(dn,1)
    dtemp(i,:)=smooth(dn(i,:),5);
end

% default parameter values are suitable for most cases
[dip]=str_dip2d(dtemp);

%plot figures
lim1=-1.2;lim2=2.7;
x1=100;y1=100;dx=400;dy=500;
figure;imagesc(dip);colormap(jet);ax = gca;
set(ax, 'CLim', [lim1 lim2]);
set(gcf,'position',[x1,y1,dx,dy]);
colorbar;xlabel('Trace','FontName','Arial','FontWeight','Bold','FontSize',14);
ylabel('Time (ms)','FontName','Arial','FontWeight','Bold','FontSize',14);
set(gca,'FontName','Arial','FontSize',14,'LineWidth',1);
title('slope field');


%% Structural smoothing
r=2;
eps=0.01;
order=2;
% dn is the input noisy data, d1 is the output smoothed data
d1=str_pwsmooth_lop2d(dn,dip,r,order,eps);



%plot figures
lim1=-1;lim2=1;
x1=100;y1=100;dx=400;dy=500;

figure;imagesc(d1);ax = gca;

set(ax, 'CLim', [lim1 lim2]);
set(gcf,'position',[x1,y1,dx,dy]);
colorbar;xlabel('Trace','FontName','Arial','FontWeight','Bold','FontSize',14);
ylabel('Time (ms)','FontName','Arial','FontWeight','Bold','FontSize',14);
set(gca,'FontName','Arial','FontSize',14,'LineWidth',1);
title('denoising result (proposed)');

figure;imagesc(dn-d1);ax = gca;

set(ax, 'CLim', [lim1 lim2]);
set(gcf,'position',[x1,y1,dx,dy]);
colorbar;xlabel('Trace','FontName','Arial','FontWeight','Bold','FontSize',14);
ylabel('Time (ms)','FontName','Arial','FontWeight','Bold','FontSize',14);
set(gca,'FontName','Arial','FontSize',14,'LineWidth',1);
title('removed noise (proposed)');

figure;imagesc(dtemp);ax = gca;

set(ax, 'CLim', [lim1 lim2]);
set(gcf,'position',[x1,y1,dx,dy]);
colorbar;xlabel('Trace','FontName','Arial','FontWeight','Bold','FontSize',14);
ylabel('Time (ms)','FontName','Arial','FontWeight','Bold','FontSize',14);
set(gca,'FontName','Arial','FontSize',14,'LineWidth',1);
title('denoising result (conventional)');

figure;imagesc(dn-dtemp);ax = gca;

set(ax, 'CLim', [lim1 lim2]);
set(gcf,'position',[x1,y1,dx,dy]);
colorbar;xlabel('Trace','FontName','Arial','FontWeight','Bold','FontSize',14);
ylabel('Time (ms)','FontName','Arial','FontWeight','Bold','FontSize',14);
set(gca,'FontName','Arial','FontSize',14,'LineWidth',1);
title('removed noise (conventional)');

snrn=str_snr(data,dn);
snr1=str_snr(data,d1);
snrc=str_snr(data,dtemp);


% write dip to excel file
xlswrite('dip.xlsx',dip);

