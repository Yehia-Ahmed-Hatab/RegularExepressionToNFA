# RegularExepressionToNFA

Thompson’s Construction that converts a
regular expressions to it’s equivalent NFA. Suppose that the alphabets Σ is the set of
ASCII characters

Listing 1: Format
Line #1 s t a t e ( s ) s e pa ra t e d by commas
e . g . : q0 , q1 , q2 , . . . , qn
Line #2 al p ha b e t s e pa ra t e d by commas
e . g . : a , b , c , e t c .
Line #3 s t a r t s t a t e
e . g . : q0
Line #4 f i n a l s t a t e ( s ) s e pa ra t e d by commas
e . g . : q0 , q1 , q2 , . . . , qn
Line #5 t r a n s i t i o n ( s ) i n a t u pl e form s e pa ra t e d by commas
( s t a r t s t a t e , alphabe t , r e s u l t s t a t e i n a r ra y form )
e . g . : ( q0 , a , [ q0 , q1 , q3 ] ) , ( q1 , b , [ q0 ] )





For example (s|ε t)* would be:
q0,q1,q2,q3,q4,q5,q6,q7,q8
 ,s,t
q0
q8
(q0, , [q8]), (q0, , [q1]), (q1, , [q2]), (q1, , [q4]), (q2, s, [q3]), (q3, , [q7]), (q4, , [q5]), (q5, t, [q6]), (q6, , [q7]), (q7, , [q1]), (q7, , [q8])
