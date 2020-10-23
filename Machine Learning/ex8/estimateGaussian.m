function [mu sigma2] = estimateGaussian(X)
%ESTIMATEGAUSSIAN This function estimates the parameters of a 
%Gaussian distribution using the data in X
%   [mu sigma2] = estimateGaussian(X), 
%   The input X is the dataset with each n-dimensional data point in one row
%   The output is an n-dimensional vector mu, the mean of the data set
%   and the variances sigma^2, an n x 1 vector
%   ���� X �́C1 �s�� n �����̃f�[�^�_�����f�[�^�Z�b�g�D 
%   �o�͂́Cn �����x�N�g�� mu�C�f�[�^�Z�b�g�̕��ςƕ��U sigma^2�Cn x 1 �̃x�N�g���D

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
% �w���B�f�[�^�̕��ςƕ��U���v�Z����
% ���ɁAmu(i)��i�Ԗڂ̓����ʂ̃f�[�^�̕��ς��܂݁Asigma2(i)��i�Ԗڂ̓����ʂ̕��U���܂ނׂ��ł���B

#size(X)
mu = sum(X)/m;
#size(mu)
sigma2 = 1/m * sum((X .- mu).^2);
sigma2 = sigma2'; # nx1
mu = mu';
#size(sigma2)







% =============================================================


end
