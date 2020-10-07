function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%
%�菇�F���̊֐��ɓ��͂��āA��������Z�b�g���g�p���Č��o���ꂽ�œK��C����уV�O�}�w�K�p�����[�^�[��Ԃ��܂��B
%svmPredict���g�p���āA��������Z�b�g�̃��x����\���ł��܂��B �Ⴆ�΁A
%�\��= svmPredict�imodel�AXval�j;
%�́A��������Z�b�g�̗\����Ԃ��܂��B
%���F�����g�p���ė\���덷���v�Z�ł��܂�
%mean�idouble�ipredictions? = yval�j�j
%
C_vec = [0.01 0.03 0.1 0.3 1 3 10]';
sigma_vec = [0.01 0.03 0.1 0.3 1 3 10]';
minError = 10000000000000000;
for i=1:length(C_vec)
  for j=1:length(sigma_vec)
    C1 = C_vec(i);
    sigma1 = sigma_vec(j);
    sim = @(x1,x2) gaussianKernel(x1,x2,sigma1);
    model = svmTrain(X,y,C1,sim);
    
    predictions = svmPredict(model,Xval);
    error_predictions = mean(double(predictions ~= yval));
    
    if error_predictions < minError
      minError = error_predictions;
      C=C1;
      sigma=sigma1;
    endif
  endfor
endfor
%fprintf('minError:%f',minError)




% =========================================================================

end
