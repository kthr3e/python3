function [U, S] = pca(X)
%PCA Run principal component analysis on the dataset X
%   [U, S, X] = pca(X) computes eigenvectors of the covariance matrix of X
%   Returns the eigenvectors U, the eigenvalues (on diagonal) in S
%
%PCAデータセットXで主成分分析を実行します
%[U、S、X] = pca（X）は、Xの共分散行列の固有ベクトルを計算します
%固有ベクトルU、Sの固有値（対角線上）を返します

% Useful values
[m, n] = size(X);

% You need to return the following variables correctly.
U = zeros(n);
S = zeros(n);

% ====================== YOUR CODE HERE ======================
% Instructions: You should first compute the covariance matrix. Then, you
%               should use the "svd" function to compute the eigenvectors
%               and eigenvalues of the covariance matrix. 
%
%手順：最初に共分散行列を計算する必要があります。 
%次に、「svd」関数を使用して、共分散行列の固有ベクトルと固有値を計算する必要があります。
%
% Note: When computing the covariance matrix, remember to divide by m (the
%       number of examples).
%注：共分散行列を計算するときは、m（例の数）で割ることを忘れないでください。
%

sigma = 1/m * X' * X;
%size(sigma)
[U,S,V] = svd(sigma);




% =========================================================================

end
