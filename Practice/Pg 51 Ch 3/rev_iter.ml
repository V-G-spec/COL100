fun rev_iter(n)=
	let fun iter(n,c)=
		if n=0 then c div 10
		else iter(n div 10,((c+n mod 10)*10))
	in iter(n,0)
	end;