fun pow(x,n)=
	if n=0 then 1
	else x*pow(x,n-1);

fun prod(a,b)=
	let fun iter(a,b,c,sum)=
		if a=0 then sum
		else iter(a div 10,b,c+1,sum+((a mod 10)*b*pow(10,c)))
	in iter(a,b,0,0)
	end