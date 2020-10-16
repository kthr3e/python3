function [U, S] = pca(X)
%PCA Run principal component analysis on the dataset X
%   [U, S, X] = pca(X) computes eigenvectors of the covariance matrix of X
%   Returns the eigenvectors U, the eigenvalues (on diagonal) in S
%
%PCA�f�[�^�Z�b�gX�Ŏ听�����͂����s���܂�
%[U�AS�AX] = pca�iX�j�́AX�̋����U�s��̌ŗL�x�N�g�����v�Z���܂�
%�ŗL�x�N�g��U�AS�̌ŗL�l�i�Ίp����j��Ԃ��܂�

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
%�菇�F�ŏ��ɋ����U�s����v�Z����K�v������܂��B 
%���ɁA�usvd�v�֐����g�p���āA�����U�s��̌ŗL�x�N�g���ƌŗL�l���v�Z����K�v������܂��B
%
% Note: When computing the covariance matrix, remember to divide by m (the
%       number of examples).
%���F�����U�s����v�Z����Ƃ��́Am�i��̐��j�Ŋ��邱�Ƃ�Y��Ȃ��ł��������B
%

sigma = 1/m * X' * X;
%size(sigma)
[U,S,V] = svd(sigma);




% =========================================================================

end
