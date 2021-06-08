fun find_div(n,test_div)=
	if test_div*test_div>n then n
	else if (n mod test_div=0) then test_div
	else find_div(n,test_div+2);

fun prime(n)=
	let
		fun smallest_div(n)=
			find_div(n,3)

	in
		(n=2) orelse ((n mod 2 =1) andalso (n=smallest_div(n)))
	end;

prime(7)
\\* Invariant: (3 <= test_div < n^(0.5) + 2)^(No odd integer in the interval [3,4,....,test_div] divides n)
