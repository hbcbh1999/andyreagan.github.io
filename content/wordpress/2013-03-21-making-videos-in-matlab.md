Title: Making videos in MATLAB
Date: 2013-03-21 16:45
Author: andyreagan
Category: General updates
Slug: making-videos-in-matlab

I've been writing a lot of code lately, and snippets of wisdom on the
web have proved very useful to me. Here's a first attempt at
contributing.

Without explanation (the comments should help), here's an example movie
made in MATLAB:

[code language="matlab"]  
% plot connected distribution at any time t

clear all

% load data in format i,tree,yield  
load N1000n1000D1.csv

max\_yeild = max(N1000n1000D1(:,1)-N1000n1000D1(:,3));  
max\_yeild\_loc =
find(N1000n1000D1(:,1)-N1000n1000D1(:,3)==max\_yeild,1);

sizes = zeros(1,length(N1000n1000D1(:,1)));

% initialize and open video writer  
writerObj = VideoWriter('test.avi');  
open(writerObj);

figure('Renderer','zbuffer');

axis tight;  
set(gca,'NextPlot','replaceChildren');

tmpfigh = gcf;  
clf;  
figshape(1000,500);

% looping over my data for the movie  
for t=4:4:length(sizes)-4

% working with my data a bit  
for i=1:length(N1000n1000D1(:,2))  
sizes(i)=length(find(N1000n1000D1(1:t,2)==i));  
end

% num\_connected(i) = number of components of length i  
num\_connected = zeros(1,length(N1000n1000D1(:,1)));

j=0;  
i=0;  
while (i \< 1000)  
i=i+1;  
if sizes(i) == 1  
connected=1;  
else  
connected=0;  
end  
len\_connected = 0;  
while (connected == 1) && (i \< 1000)  
len\_connected = len\_connected + 1;  
i=i+1;  
if sizes(i) == 1  
connected=1;  
else  
connected=0;  
end  
end  
if len\_connected  
j=j+1;  
num\_connected(j)=len\_connected;  
%num\_connected(len\_connected)=num\_connected(len\_connected)+1;  
end  
end  
subplot(1,2,1)  
% plot red when near the maximum yield  
if t \> max\_yeild-5 && t \< max\_yield+5  
fig1 =
plot(1:find(num\_connected==0,1)-1,sort(num\_connected(1:find(num\_connected==0,1)-1),'descend'),'r.');  
else  
fig1 =
plot(1:find(num\_connected==0,1)-1,sort(num\_connected(1:find(num\_connected==0,1)-1),'descend'),'b.');  
end

xlim([1 250])  
ylim([0 100])  
xlabel('Size of connected component')  
ylabel('Number of connected components')  
title('D=1 Connected Component Distribution')

subplot(1,2,2)  
plot(N1000n1000D1(:,1),N1000n1000D1(:,1)-N1000n1000D1(:,3),'b.');  
xlim([1 1000]);  
hold on;  
plot([t+4 t+4],[0 1000],'r-')  
hold off;  
xlabel('Timestep')  
ylabel('Yield')  
title('D=1 Yeild Curve')

% write out the video  
frame = getframe(gcf);  
writeVideo(writerObj,frame);

end

close(writerObj);  
[/code]

If this helped, please let me know in the comments. Cheers.

Here is the output: https://vimeo.com/62371566
