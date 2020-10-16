function Z = projectData(X, U, K)
%PROJECTDATA Computes the reduced data representation when projecting only 
%on to the top k eigenvectors
%   Z = projectData(X, U, K) computes the projection of 
%   the normalized inputs X into the reduced dimensional space spanned by
%   the first K columns of U. It returns the projected examples in Z.
%
%PROJECTDATA���k�̌ŗL�x�N�g���݂̂Ɏˉe����ꍇ�̏k���f�[�^�\�����v�Z���܂�
%Z = projectData�iX�AU�AK�j�́A���K�����ꂽ����X�́A
%U�̍ŏ���K��ɂ܂�����k��������Ԃւ̎ˉe���v�Z���܂��B�ˉe���ꂽ���Z�ŕԂ��܂��B

% You need to return the following variables correctly.
Z = zeros(size(X, 1), K);

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the projection of the data using only the top K 
%               eigenvectors in U (first K columns). 
%               For the i-th example X(i,:), the projection on to the k-th 
%               eigenvector is given as follows:
%                    x = X(i, :)';
%                    projection_k = x' * U(:, k);
%
%�菇�FU�̏��K�̌ŗL�x�N�g���i�ŏ���K��j�݂̂��g�p���ăf�[�^�̎ˉe���v�Z���܂��B
%i�Ԗڂ̗�X�ii�A:)�̏ꍇ�Ak�Ԗڂ̌ŗL�x�N�g���ւ̎ˉe�͎��̂悤�ɗ^�����܂��B
Ureduce = U(:,1:K);
%size(Ureduce) 2 1
Z = X * Ureduce;
 


% =============================================================

end
