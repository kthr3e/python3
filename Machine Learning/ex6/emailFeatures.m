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
%               �菇�F���̊֐��ɓ��͂��āA�w�肳�ꂽ�d�q���[���̓����x�N�g���iword_indices�j��Ԃ��܂��B
%               �d�q���[���̏�����e�Ղɂ��邽�߂ɁA���łɊe�d�q���[����O�������A
%               �d�q���[�����̊e�P����Œ莫���i1899��j�̃C���f�b�N�X�ɕϊ����܂����B
%               �ϐ�word_indices�ɂ́A1�̓d�q���[���Ɋ܂܂��P��̃C���f�b�N�X�̃��X�g���܂܂�Ă��܂��B
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
%              ���Ȃ��̃^�X�N�́A���̂悤��word_indices�x�N�g����1���A����̒P�ꂪ�d�q���[���ɏo�����邩�ǂ����������o�C�i�������x�N�g�����\�z���邱�Ƃł��B
%              �܂�A�P��i���d�q���[���ɑ��݂���ꍇ�Ax�ii�j= 1�ł��B
%              ��̓I�ɂ́A�uthe�v�Ƃ����P��i���Ƃ��΁A�C���f�b�N�X60�j���d�q���[���Ɋ܂܂�Ă���ꍇ�Ax�i60�j= 1�ł��B
%              �����x�N�g���͎��̂悤�ɂȂ�܂��B              
%
%              x = [ 0 0 0 0 1 0 0 0 ... 0 0 0 0 1 ... 0 0 0 1 0 ..];
%
%

for i = word_indices
  x(i) = 1;
endfor





% =========================================================================
    

end
