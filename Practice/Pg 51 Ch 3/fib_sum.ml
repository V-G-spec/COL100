fun sum_fib(n)=
	    if n=1 then 1
		else if n=2 then 2
		else 
			let
				fun fib(n,a1,a2,sum)=
				if n=2 then sum
				else fib(n-1,a2,a1+a2,sum+a1+a2)
			in fib(n,1,1,2)
	end;
