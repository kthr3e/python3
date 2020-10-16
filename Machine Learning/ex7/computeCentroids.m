function centroids = computeCentroids(X, idx, K)
%COMPUTECENTROIDS returns the new centroids by computing the means of the 
%data points assigned to each centroid.
%   centroids = COMPUTECENTROIDS(X, idx, K) returns the new centroids by 
%   computing the means of the data points assigned to each centroid. It is
%   given a dataset X where each row is a single data point, a vector
%   idx of centroid assignments (i.e. each entry in range [1..K]) for each
%   example, and K, the number of centroids. You should return a matrix
%   centroids, where each row of centroids is the mean of the data points
%   assigned to it.
%
%COMPUTECENTROIDSは、各セントロイドに割り当てられたデータポイントの平均を計算することにより、新しいセントロイドを返します。
%centroids = COMPUTECENTROIDS（X、idx、K）は、各重心に割り当てられたデータポイントの平均を計算することにより、新しい重心を返します。
%各行が単一のデータポイントであるデータセットX、各例の重心割り当てのベクトルidx（つまり、範囲[1..K]の各エントリ）、およびK（重心の数）が与えられます。
%行列の重心を返す必要があります。ここで、重心の各行は、それに割り当てられたデータポイントの平均です。

% Useful variables
[m n] = size(X);

% You need to return the following variables correctly.
centroids = zeros(K, n);


% ====================== YOUR CODE HERE ======================
% Instructions: Go over every centroid and compute mean of all points that
%               belong to it. Concretely, the row vector centroids(i, :)
%               should contain the mean of the data points assigned to
%               centroid i.
%
%手順：すべての図心を調べて、それに属するすべての点の平均を計算します。
%具体的には、行ベクトルcentroids（i、:)には、
%centroid iに割り当てられたデータポイントの平均が含まれている必要があります。
%
% Note: You can use a for-loop over the centroids to compute this.
%
count = zeros(size(centroids),1); % 重心に近いXが何個あるか
for i = 1:m
  centroids(idx(i),:) += X(i,:);
  count(idx(i))+=1;
endfor

centroids = centroids./count;



% =============================================================


end

