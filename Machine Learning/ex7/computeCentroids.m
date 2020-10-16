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
%COMPUTECENTROIDS�́A�e�Z���g���C�h�Ɋ��蓖�Ă�ꂽ�f�[�^�|�C���g�̕��ς��v�Z���邱�Ƃɂ��A�V�����Z���g���C�h��Ԃ��܂��B
%centroids = COMPUTECENTROIDS�iX�Aidx�AK�j�́A�e�d�S�Ɋ��蓖�Ă�ꂽ�f�[�^�|�C���g�̕��ς��v�Z���邱�Ƃɂ��A�V�����d�S��Ԃ��܂��B
%�e�s���P��̃f�[�^�|�C���g�ł���f�[�^�Z�b�gX�A�e��̏d�S���蓖�Ẵx�N�g��idx�i�܂�A�͈�[1..K]�̊e�G���g���j�A�����K�i�d�S�̐��j���^�����܂��B
%�s��̏d�S��Ԃ��K�v������܂��B�����ŁA�d�S�̊e�s�́A����Ɋ��蓖�Ă�ꂽ�f�[�^�|�C���g�̕��ςł��B

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
%�菇�F���ׂĂ̐}�S�𒲂ׂāA����ɑ����邷�ׂĂ̓_�̕��ς��v�Z���܂��B
%��̓I�ɂ́A�s�x�N�g��centroids�ii�A:)�ɂ́A
%centroid i�Ɋ��蓖�Ă�ꂽ�f�[�^�|�C���g�̕��ς��܂܂�Ă���K�v������܂��B
%
% Note: You can use a for-loop over the centroids to compute this.
%
count = zeros(size(centroids),1); % �d�S�ɋ߂�X�������邩
for i = 1:m
  centroids(idx(i),:) += X(i,:);
  count(idx(i))+=1;
endfor

centroids = centroids./count;



% =============================================================


end

