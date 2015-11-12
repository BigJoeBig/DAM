function [centers, IsRed] = Proj(  )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
I = imread('image2.png');
Org = I;
I = bw(I);
%I = imsharpen(I,'Radius',2,'Amount',2);
I = EdgeSpaltial(I);

%imshow(I);


[centers, radii] = imfindcircles(I,[30 40], 'ObjectPolarity', ...
    'dark', 'Sensitivity',0.92, 'Method','twostage', 'EdgeThreshold',0.04);



imshow(Org);
viscircles(centers, radii,'EdgeColor','b');
R = I(:,:,1);

for i=1:length(centers)
  %  disp(R(floor(centers(i,1)), floor(centers(i,2))));
  if R(floor(centers(i,2)), floor(centers(i,1))) > 0
      IsRed(i) = true;
  else
      IsRed(i) = false;
  end

end

disp(IsRed);

fileID = fopen('exp.txt','w');

for i=1:length(IsRed)
    fprintf(fileID,'%d\n', floor(centers(i,1)));
    fprintf(fileID,'%d\n', floor(centers(i,2)));
    fprintf(fileID,'%d\n', IsRed(i));

end

fclose(fileID);

end

