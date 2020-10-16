function Z = projectData(X, U, K)
%PROJECTDATA Computes the reduced data representation when projecting only 
%on to the top k eigenvectors
%   Z = projectData(X, U, K) computes the projection of 
%   the normalized inputs X into the reduced dimensional space spanned by
%   the first K columns of U. It returns the projected examples in Z.
%
%PROJECTDATA上位k個の固有ベクトルのみに射影する場合の縮小データ表現を計算します
%Z = projectData（X、U、K）は、正規化された入力Xの、
%Uの最初のK列にまたがる縮小次元空間への射影を計算します。射影された例をZで返します。

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
%手順：Uの上位K個の固有ベクトル（最初のK列）のみを使用してデータの射影を計算します。
%i番目の例X（i、:)の場合、k番目の固有ベクトルへの射影は次のように与えられます。
Ureduce = U(:,1:K);
%size(Ureduce) 2 1
Z = X * Ureduce;
 


% =============================================================

end
