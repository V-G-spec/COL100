# PROBLEM 1.1:

fun add(a,b)=
	a+b;

fun mult(a,b) =
	if (b = 0) then 0
	else
		let
			fun iter(a,b,i,k) = 
				if (i = a) then k
				else iter(a,b,add(i,1),add(k,b))
		in
			iter(a,b,0,0)
		end;

# Invariant: (0<=i<=a)^(k=i*b)




# PROBLEM 1.2:

# a. Time Complexity

# Time taken to calculate a*b solely depends upon a
# i.e.
# T(a)=T(a-1) + 1 {The +1 is for the testing condition}
#    =T(a-2) + 1 + 1 = T(a-2) +2
#   .
#   .
#   .
#   .
# T(a)=T(0) + a

# Let T(0)=1
# => T(a)= a + 1



# b. Space Complexity
# 	O(1)	




# PROBLEM 1.3


fun mult(a,b)=
     if b=0 then 0
     else
	let fun iter(a,b,i,k)=
		if i=0 then a
		else if (even(i)) then iter(a,b,halve(i), double(k))		
		else iter(add(a,k),b,halve(dec(i)), double(k))
	in iter(0,b,b,a)
	end;

# Time complexity: O(log n)  [=O((log n)/(log 2))] 
# Invariant: (0<=i<=b)^(After m iterations, i= (b div 2^m))^(k=(2^m * k0))^(i*k + a = a0 * b0)






# PROBLEM 4



fun intsqrt(n) =
let fun maxpow(n) =
	if (n div 4 = 0) then 1
	else 4*maxpow(n div 4);

     fun iter(i,n,c) =
   	if (c = 0) then i
	else if (2*i+1)*(2*i+1) > (n div c) then iter(2*i,n,c div 4)
	else iter(2*i+1,n,c div 4);
in
	iter(0,n,maxpow(n))
end;


# Invariant (Given in question): c0=4^k0 such that n div (4^k0) > 0 and n div (4^k0 + 1) =0. After k iterations, 0<=k<=k0, c = c0 div (4^k) and i^2 <= n div (c*4) < (i+1)^2.

# Since every iteration reduces k to k div 4. Therefore T(n)=O(log n) [=O((log n)/(log 4))]





# Prime (Method 1)



fun find_div(n,test_div)=
	if test_div*test_div>n then n
	else if (n mod test_div=0) then test_div 
	else find_div(n,test_div+2);

fun prime(n)=
	let
		fun smallest_div(n)=
			find_div(n,3)
			
	in 
		(n=2) orelse ((n mod 2 =1) andalso (n=smallest_div(n)))
	end;

# Invariant: (3 <= test_div < n^(0.5) + 2)^(No odd integer in the interval [3,4,....,test_div] divides n)




# Prime (Method 2)



fun prime(n,q)=
	let 
		fun prime_test(n,q,failed)=
			let 
				fun fermat_test(n)=
					let
						fun expmod(b,e,m)=
							let
								fun sqr(x)= x*x :int;
							in 
								if e=0 then 1
								else if (e mod 2)=0 then sqr(expmod(b,e div 2,m)) mod m
								else ((b mod m) * expmod(b,e-1,m)) mod m
							end
					in 
						let
							 val q= Random.randRange(3,n-1);
							 val p= Random.rand(1,1);
							 val a= q p
						in 
							(1=expmod(a,n-1,n))
						end
					end
			in 
				if q=0 then true
				else if failed then false
				else prime_test(n,q-1,not(fermat_test(n)))
			end
	in 
		if (n=2) then true
		else prime_test(n,q,false)
	end;	



# Invariant= (Not failed = (n has passed Fermat's test (q0 - q) times)) 