function [mu sigma2] = estimateGaussian(X)
%ESTIMATEGAUSSIAN This function estimates the parameters of a 
%Gaussian distribution using the data in X
%   [mu sigma2] = estimateGaussian(X), 
%   The input X is the dataset with each n-dimensional data point in one row
%   The output is an n-dimensional vector mu, the mean of the data set
%   and the variances sigma^2, an n x 1 vector
%   入力 X は，1 行に n 次元のデータ点を持つデータセット． 
%   出力は，n 次元ベクトル mu，データセットの平均と分散 sigma^2，n x 1 のベクトル．

% Useful variables
[m, n] = size(X);

% You should return these values correctly
mu = zeros(n, 1);
sigma2 = zeros(n, 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the mean of the data and the variances
%               In particular, mu(i) should contain the mean of
%               the data for the i-th feature and sigma2(i)
%               should contain variance of the i-th feature.
%
% 指示。データの平均と分散を計算する
% 特に、mu(i)はi番目の特徴量のデータの平均を含み、sigma2(i)はi番目の特徴量の分散を含むべきである。

#size(X)
mu = sum(X)/m;
#size(mu)
sigma2 = 1/m * sum((X .- mu).^2);
sigma2 = sigma2'; # nx1
mu = mu';
#size(sigma2)







% =============================================================


end
