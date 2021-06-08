fun f(x,y)=
	let
		fun div_i(x,y)=
			if (x-y<0) then x
			else div_i(x-y,y)
	in div_i(x,y)
end			
