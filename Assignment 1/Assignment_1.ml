fun fact(n)=
	let
		fun fact_iter(m,f,c)=
		if c=m then f
		else fact_iter(m,f*(c+1),c+1)
	in fact_iter(n,1,0)
end;



fun fact_rec(n)=
if n=0 then 1
else n*fact_rec(n-1);



fun fib(n)=
	if n=1 then 1
	else if n=2 then 1
	else
		let fun fib_iter(n,sum,a1,a2)=
			if n=3 then sum
			else fib_iter(n-1,sum+a2,a2,a1+a2)
		in fib_iter(n,2,1,1)
		end;



fun fib(n)=
if n=0 then 1
else
    if n=1 then 1
else
    fib(n-1)+fib(n-2);




fun perfect(n)=
	let
		fun addfactors(n)=
			let 
				fun f(n,i)=
					if (n mod i=0) then i else 0;
				fun sum(f,a,b,n)=
					if (a>b) then 0
					else f(n,b) + sum(f,a,b-1,n)
			in
				sum(f,1,n div 2, n)
			end
	in
		(n=addfactors(n))
	end;




fun pow_iter(x,n)=
	let fun p_iter(p,m)=
		if (m=0) then p
		else p_iter(p*x,m-1)
	in p_iter(1,n)
end;




fun pow_rec(x,n)=
if n=0 then 1
else x*pow_rec(x,n-1);




fun sqrt(n)=
	if n=0 then 0 
	else
		 
		  if (2*sqrt(n div 4)+1)*(2*sqrt(n div 4)+1)<=n then 2*sqrt(n div 4)+1
		  else 2*sqrt(n div 4); 
			
