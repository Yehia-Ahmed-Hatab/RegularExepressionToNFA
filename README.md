# RegularExepressionToNFA

Thompson’s Construction that converts a
regular expressions to it’s equivalent NFA. Suppose that the alphabets Σ is the set of
ASCII characters

Listing 1: Format  
Line #1 state(s) separated by commas  
e . g . : q0 , q1 , q2 , . . . , qn  
Line #2 alphabet separated by commas  
e . g . : a , b , c , e t c .  
Line #3 start state  
e . g . : q0  
Line #4 final state(s) separated by commas  
e . g . : q0 , q1 , q2 , . . . , qn  
Line #5 transition(s) in a tuple form separated by commas  
( start state , alphabet , result state in array form )  
e . g . : ( q0 , a , [ q0 , q1 , q3 ] ) , ( q1 , b , [ q0 ] )  





For example (s|ε t)* would be:  
q0,q1,q2,q3,q4,q5,q6,q7,q8  
 ,s,t  
q0  
q8  
(q0, , [q8]), (q0, , [q1]), (q1, , [q2]), (q1, , [q4]), (q2, s, [q3]), (q3, , [q7]), (q4, , [q5]), (q5, t, [q6]), (q6, , [q7]), (q7, , [q1]), (q7, , [q8])  
