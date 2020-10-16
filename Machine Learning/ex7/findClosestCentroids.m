function idx = findClosestCentroids(X, centroids)
%FINDCLOSESTCENTROIDS computes the centroid memberships for every example
%   idx = FINDCLOSESTCENTROIDS (X, centroids) returns the closest centroids
%   in idx for a dataset X where each row is a single example. idx = m x 1 
%   vector of centroid assignments (i.e. each entry in range [1..K])
%

% Set K
K = size(centroids, 1);

% You need to return the following variables correctly.
idx = zeros(size(X,1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Go over every example, find its closest centroid, and store
%               the index inside idx at the appropriate location.
%               Concretely, idx(i) should contain the index of the centroid
%               closest to example i. Hence, it should be a value in the 
%               range 1..K
%
%手順：すべての例に目を通し、最も近い重心を見つけて、idx内の適切な場所にインデックスを保存します。
%具体的には、idx（i）には、例iに最も近い重心のインデックスが含まれている必要があります。 
%したがって、1..Kの範囲の値である必要があります。
%
% Note: You can use a for-loop over the examples to compute this.
%

for i = 1:size(X,1)
  len = sum((X(i,:) - centroids(1,:)) .^2);
  idx(i) = 1;
  for j = 1:K
    if len > sum((X(i,:) - centroids(j,:)) .^2)
      len = sum((X(i,:) - centroids(j,:)) .^2);
      idx(i) = j;
    endif
  endfor
endfor







% =============================================================

end

