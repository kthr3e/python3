function x = emailFeatures(word_indices)
%EMAILFEATURES takes in a word_indices vector and produces a feature vector
%from the word indices
%   x = EMAILFEATURES(word_indices) takes in a word_indices vector and 
%   produces a feature vector from the word indices. 

% Total number of words in the dictionary
n = 1899;

% You need to return the following variables correctly.
x = zeros(n, 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return a feature vector for the
%               given email (word_indices). To help make it easier to 
%               process the emails, we have have already pre-processed each
%               email and converted each word in the email into an index in
%               a fixed dictionary (of 1899 words). The variable
%               word_indices contains the list of indices of the words
%               which occur in one email.
%               手順：この関数に入力して、指定された電子メールの特徴ベクトル（word_indices）を返します。
%               電子メールの処理を容易にするために、すでに各電子メールを前処理し、
%               電子メール内の各単語を固定辞書（1899語）のインデックスに変換しました。
%               変数word_indicesには、1つの電子メールに含まれる単語のインデックスのリストが含まれています。
%
%               Concretely, if an email has the text:
%
%                  The quick brown fox jumped over the lazy dog.
%
%               Then, the word_indices vector for this text might look 
%               like:
%               
%                   60  100   33   44   10     53  60  58   5
%
%               where, we have mapped each word onto a number, for example:
%
%                   the   -- 60
%                   quick -- 100
%                   ...
%
%              (note: the above numbers are just an example and are not the
%               actual mappings).
%
%              Your task is take one such word_indices vector and construct
%              a binary feature vector that indicates whether a particular
%              word occurs in the email. That is, x(i) = 1 when word i
%              is present in the email. Concretely, if the word 'the' (say,
%              index 60) appears in the email, then x(60) = 1. The feature
%              vector should look like:
%               
%              あなたのタスクは、そのようなword_indicesベクトルを1つ取り、特定の単語が電子メールに出現するかどうかを示すバイナリ特徴ベクトルを構築することです。
%              つまり、単語iが電子メールに存在する場合、x（i）= 1です。
%              具体的には、「the」という単語（たとえば、インデックス60）が電子メールに含まれている場合、x（60）= 1です。
%              特徴ベクトルは次のようになります。              
%
%              x = [ 0 0 0 0 1 0 0 0 ... 0 0 0 0 1 ... 0 0 0 1 0 ..];
%
%

for i = word_indices
  x(i) = 1;
endfor





% =========================================================================
    

end
