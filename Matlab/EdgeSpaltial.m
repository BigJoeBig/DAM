function [OutI] = EdgeSpaltial(I)

% Read image

% Normalise to a [0, 1] range
I = double(I) / 255;

% Create matrices for storing directional gradients
OutSx = zeros(size(I));
OutSy = zeros(size(I));

% Create convolution kernels
Sx = [-1 0 1 ; -2 0 2 ; -1 0 1];
Sy = [1 2 1 ; 0 0 0 ; -1 -2 -1];

% Apply the convolution
for y=1:size(I, 1)
    for x=1:size(I, 2)
        for i=1:size(Sx, 1)
            for j=1:size(Sx, 2)
                if(y+i-2 > 0 && x+j-2 > 0 ...
                   && y+i-2 <= size(I, 1) && x+j-2 <= size(I, 2))
                    OutSx(y,x) = OutSx(y,x) + Sx(i,j) * I(y+i-2, x+j-2);
                    OutSy(y,x) = OutSy(y,x) + Sy(i,j) * I(y+i-2, x+j-2);
                end
            end
        end
    end
end

% Output the magnitude of the two directional gradients
OutI = sqrt(OutSx .^ 2 + OutSy .^ 2);
imshow(OutI);

end
