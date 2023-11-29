OPENQASM 2.0;
include "qelib1.inc";
gate mcx q0,q1,q2,q3 { h q3; p(pi/8) q0; p(pi/8) q1; p(pi/8) q2; p(pi/8) q3; cx q0,q1; p(-pi/8) q1; cx q0,q1; cx q1,q2; p(-pi/8) q2; cx q0,q2; p(pi/8) q2; cx q1,q2; p(-pi/8) q2; cx q0,q2; cx q2,q3; p(-pi/8) q3; cx q1,q3; p(pi/8) q3; cx q2,q3; p(-pi/8) q3; cx q0,q3; p(pi/8) q3; cx q2,q3; p(-pi/8) q3; cx q1,q3; p(pi/8) q3; cx q2,q3; p(-pi/8) q3; cx q0,q3; h q3; }
qreg f7[1];
qreg f6[1];
qreg f5[1];
qreg f4[1];
qreg f3[1];
qreg f2[1];
qreg f1[1];
qreg f0[1];
qreg x11[1];
qreg x10[1];
qreg x9[1];
qreg x8[1];
qreg x7[1];
qreg x6[1];
qreg x5[1];
qreg x4[1];
qreg x3[1];
qreg x2[1];
qreg x1[1];
qreg x0[1];
mcx x3[0],x7[0],x11[0],f3[0];
x f0[0];
x f1[0];
x f2[0];
x f3[0];
mcx x2[0],x6[0],x11[0],f2[0];
mcx x1[0],x5[0],x11[0],f1[0];
mcx x0[0],x4[0],x11[0],f0[0];
mcx x3[0],x7[0],x10[0],f3[0];
ccx x3[0],x10[0],f3[0];
mcx x2[0],x6[0],x10[0],f2[0];
ccx x2[0],x10[0],f2[0];
mcx x1[0],x5[0],x10[0],f1[0];
ccx x1[0],x10[0],f1[0];
mcx x0[0],x4[0],x10[0],f0[0];
ccx x0[0],x10[0],f0[0];
x x2[0];
x x8[0];
mcx x2[0],x6[0],x8[0],f6[0];
x x6[0];
x x9[0];
mcx x2[0],x6[0],x9[0],f6[0];
x x1[0];
mcx x1[0],x5[0],x8[0],f5[0];
x x5[0];
mcx x1[0],x5[0],x9[0],f5[0];
x x0[0];
mcx x0[0],x4[0],x8[0],f4[0];
x x4[0];
mcx x0[0],x4[0],x9[0],f4[0];
x x3[0];
mcx x3[0],x7[0],x8[0],f7[0];