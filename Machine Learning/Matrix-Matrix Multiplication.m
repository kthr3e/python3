% Initialize a 3 by 2 matrix
A = [1, 2; 3, 4;5, 6]

% Initialize a 2 by 1 matrix
B = [1; 2]

% We expect a resulting matrix of (3 by 2)*(2 by 1) = (3 by 1)
mult_AB = A*B

% Make sure you understand why we got that result
>> B = [-30,0.25;10,5]
B =

  -30.00000    0.25000
   10.00000    5.00000

>> mult_AB=A*B
mult_AB =

  -10.000   10.250
  -50.000   20.750
  -90.000   31.250

% f1(x)=-30+10x f2(x)=0.25+5x
