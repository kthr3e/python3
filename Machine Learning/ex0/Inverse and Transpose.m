>> A = [1,2,0;0,5,6;7,0,9]
A =

   1   2   0
   0   5   6
   7   0   9

>> A_trans=A'
A_trans =

   1   0   7
   2   5   0
   0   6   9

>> A_inv=inv(A)
A_inv =

   0.348837  -0.139535   0.093023
   0.325581   0.069767  -0.046512
  -0.271318   0.108527   0.038760

>> A_invA=inv(A)*A
A_invA =

   1.0000e+00  -8.3267e-17   5.5511e-17
   2.7756e-17   1.0000e+00  -8.3267e-17
  -3.4694e-17   2.7756e-17   1.0000e+00

>> A_transA*=A_trans*A_inv
error: in computed assignment A OP= X, A must be defined first
>> A_transAA_inv=A_trans*A_inv
A_transAA_inv =

  -1.550388   0.620155   0.364341
   2.325581   0.069767  -0.046512
  -0.488372   1.395349   0.069767

>> u=[4;-4;-3]
u =

   4
  -4
  -3

>> U=[4;-4;-3]
U =

   4
  -4
  -3

>> V=[4;2;4]
V =

   4
   2
   4

>> U_tra=U'
U_tra =

   4  -4  -3

>> ans=U_tra*V
ans = -4
