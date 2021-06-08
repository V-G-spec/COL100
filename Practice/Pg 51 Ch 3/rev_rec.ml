fun rev_rec(n)=
	if n=0 then 0
	else rev_rec(n) = (n%10 * pow(10, digits)) + reverse(n/10);

//Where pow(x,y) calculates x^y and digits is number of digits in the number//
		