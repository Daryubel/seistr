test_2D_SOF;

dataF = data;

for i=1:1:size(dataF, 2)
    for j=1:1:size(dataF, 1)
        if abs(dip(j,i)) < 0.1
            dataF(j,i) = 0;
        end
    end
end

x1=100;y1=100;dx=400;dy=500;

figure;imagesc(dataF);ax = gca;
set(ax, 'CLim', [lim1 lim2]);
set(gcf,'position',[x1,y1,dx,dy]);
colorbar;xlabel('Trace','FontName','Arial','FontWeight','Bold','FontSize',14);
ylabel('Time (ms)','FontName','Arial','FontWeight','Bold','FontSize',14);
set(gca,'FontName','Arial','FontSize',14,'LineWidth',1);
title('PWD Filtered');

xlswrite('PWDF.xlsx',dip);

