fun f(n)=
	let
		fun count(n,c)=
			if (n=0) then c
			else count(n div 10,c+1)
	in count(n,0)
end			
			
