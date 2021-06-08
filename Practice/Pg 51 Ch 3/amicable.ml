fun amic(x,y)=
	
	let
		fun div_sum(n)=
			let 
				fun f(n,i)=
					if (n mod i=0) then i else 0;
				fun sum(f,a,b,n)=
					if (a>b) then 0
					else f(n,b) + sum(f,a,b-1,n)
			in
				sum(f,1,n div 2, n)
			end
	
	
	in (x=div_sum(y) andalso y=div_sum(x))
end;	
