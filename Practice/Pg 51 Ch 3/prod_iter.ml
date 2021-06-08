fun f(n,x)=
	let
		fun prod(n,c,x)=
			if (n=0) then c
			else prod(n-1,c+x,x)
	in prod(n,0,x)
end			
