function [J, grad] = cofiCostFunc(params, Y, R, num_users, num_movies, ...
                                  num_features, lambda)
%COFICOSTFUNC Collaborative filtering cost function
%   [J, grad] = COFICOSTFUNC(params, Y, R, num_users, num_movies, ...
%   num_features, lambda) returns the cost and gradient for the
%   collaborative filtering problem.
%
%COFICOSTFUNC �����t�B���^�����O�R�X�g�֐�
% [J, grad] = COFICOSTFUNC(params, Y, R, num_users, num_movies, ...
%num_features, lambda) �����t�B���^�����O���̃R�X�g�ƌ��z��Ԃ��܂��B

% Unfold the U and W matrices from params
X = reshape(params(1:num_movies*num_features), num_movies, num_features);
Theta = reshape(params(num_movies*num_features+1:end), ...
                num_users, num_features);

            
% You need to return the following values correctly
J = 0;
X_grad = zeros(size(X));
Theta_grad = zeros(size(Theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost function and gradient for collaborative
%               filtering. Concretely, you should first implement the cost
%               function (without regularization) and make sure it is
%               matches our costs. After that, you should implement the 
%               gradient and use the checkCostFunction routine to check
%               that the gradient is correct. Finally, you should implement
%               regularization.
%
% Notes: X - num_movies  x num_features matrix of movie features
%        Theta - num_users  x num_features matrix of user features
%        Y - num_movies x num_users matrix of user ratings of movies
%        R - num_movies x num_users matrix, where R(i, j) = 1 if the 
%            i-th movie was rated by the j-th user
%
%�w���B�����t�B���^�����O�̂��߂̃R�X�g�֐��ƌ��z���v�Z���܂��B
%��̓I�ɂ́A�܂��R�X�g�֐����������āi�����������Ɂj�A���ꂪ�R�X�g�ƈ�v���邱�Ƃ��m�F���Ă��������B
%���̏��,���z�����������ǂ������`�F�b�N���邽�߂ɁAcheckCostFunction ���[�`�����g�p���܂��B
%�Ō�ɁA���������������܂��傤�B
%
% You should set the following variables correctly:
%�ȉ��̕ϐ��𐳂����ݒ肷��K�v������܂��B
%        X_grad - num_movies x num_features matrix, containing the 
%                 partial derivatives w.r.t. to each element of X
%X_grad - num_movies x num_features �s��CX �̊e�v�f�ɑ΂��镔�����֐����܂݂܂��D

%
%        Theta_grad - num_users x num_features matrix, containing the 
%                     partial derivatives w.r.t. to each element of Theta
%         Theta_grad - num_users x num_features �̍s��D
%

%size(Theta) 4x3
%size(X)   5x3
J = 1/2 * sum(sum((X*Theta' - Y).^2 .* R));
%Regularized cost function
J += lambda/2 * (sum(sum( Theta.^2)) + sum(sum(X.^2)));
X_grad = (X * Theta' - Y).* R * Theta + lambda * X;
Theta_grad = ((X * Theta' - Y).* R)' * X + lambda * Theta;












% =============================================================

grad = [X_grad(:); Theta_grad(:)];

end
