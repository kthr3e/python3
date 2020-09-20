function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

%A1 5000 x 401
A1 = [ones(m, 1) X];
%Y [0,0,... ,1,...,0]
Y = zeros(m,num_labels);
for i=1:m
  Y(i,y(i))=1;
endfor

 %h(x)
 %A2_s=size(A2) %5000x25
Z2 = A1 * Theta1';
A2 = sigmoid(Z2);
%add bias
a2 = size(A2,1);
A2 = [ones(a2,1) A2];
% size(A2) 5000x26

%size(A3) 5000x10
Z3 = A2 * Theta2';
A3 = sigmoid(Z3);
h = A3;

%Cost Function
for i=1:m
  for k=1:num_labels
    J+= -Y(i,k) * log(h(i,k)) - (1-Y(i,k)) * log(1-h(i,k));
  endfor
endfor

J=J/m;


%Regularuzation
R=0;

for j=1:size(Theta1,1)
  for k=2:size(Theta1,2)  
    R+=Theta1(j,k)^2;
  endfor
endfor

for j=1:size(Theta2,1)
  for k=2:size(Theta2,2)  
    R+=Theta2(j,k)^2;
  endfor
endfor

% óÒêîÇÃîÕàÕéwíËÇÃÇ‚ÇËï˚Ç™ÇÌÇ©ÇÁÇ»Ç¢ÇΩÇﬂÇ≈Ç´Ç»Ç©Ç¡ÇΩÇ‚Ç¬
##R +=sum(sum(Theta1.^2)) + sum(sum(Theta2.^2)) - Theta1(:,1).^2 - Theta2(:,1).^2;

J+=lambda/(2*m) * R;

% Backpropagation
%åÎç∑ÇåvéZ
%5000x10
delta3 = h - Y;
% 5000x26
delta2 = delta3 * Theta2;
%5000x25
delta2 = delta2(:,2:end);
delta2 = delta2 .* sigmoidGradient(Z2);

%åÎç∑Ç©ÇÁïŒî˜ï™ÇÃÇ‡Ç∆Ç∆Ç»ÇÈÇ‡ÇÃÇåvéZ
%10x26
Delta2 = delta3' * A2;
%25x401
Delta1 = delta2' * A1;

Theta1_grad = Delta1/m;
Theta2_grad = Delta2/m;

%Regularuzation
Theta1_grad(:,2:end) += lambda/m * Theta1(:,2:end);
Theta2_grad(:,2:end) += lambda/m * Theta2(:,2:end);




% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
