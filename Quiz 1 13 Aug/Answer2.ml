(*Answer 2*)
exception Neg_Input_Not_Valid
fun power (x, 0) = 1  
    | power (x, n) = x * power(x, n-1);

fun numofdig(0) = 0
	| numofdig(n) = 1+ numofdig(n div 10);

fun revrec(n) = if n=0 then 0
	else if n>0 then (n mod 10)*power(10,numofdig(n)-1) + revrec(n div 10)
	else raise Neg_Input_Not_Valid;

(*Number of steps required:*)
(*In every step, the variable n gets updated as (n div 10)*)
(*Therefore, total steps = (number of digits in n) + 1 (Base condition step)*)
(*= floor((log n)/(log 10)) + 1 + 1 = floor((log n)/(log 10)) + 2*)