fun isprime(n)=
	let fun isdivisor(x,i)=
			if x=2 then true
			else if (x mod i = 0) then false
			else if (i*i>=x) then true
			else isdivisor(x,i+1)
	in isdivisor(n,2)
	end;
