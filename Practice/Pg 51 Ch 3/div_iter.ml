fun f(x,n)=
	let
		fun div_i(x,n,c)=
			if (x-n<0) then c
			else div_i(x-n,n,c+1)
	in div_i(x,n,0)
end			
