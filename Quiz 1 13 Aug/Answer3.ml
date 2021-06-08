(*Answer 3*)

exception Input_Not_Valid
fun frog(n)=
	if n<=0 then raise Input_Not_Valid
	else if n=1 then 1 else if n=2 then 2 else if n=3 then 4
	else frog(n-1) + frog(n-2) + frog(n-3);


(*Induction Hypothesis: frog(k) for 1<=k<n returns number of ways frogs can jump up to the kth step *)
(*Induction Step:*)
(*  Since the frogs can only take 1,2 or 3 steps at a time  *)
(*  Total number of steps would be steps taken for reaching n-1 stairs (_,_,_,_,...,1)  *)
(*  +for reaching n-2 stairs (_,_,_,_,...,2)  *)
(*  +for reaching n-3 stairs (_,_,_,_,...,3)  *)
(*  Where the number of blanks are n-1, n-2, n-3 respectively  *)



fun frog_fast(n:real)=
	if floor(n)<=0 then raise Input_Not_Valid
	else if floor(n)=1 then 1.0 else if floor(n)=2 then 2.0 else if floor(n)=3 then 4.0
	else
		let fun iter_fast(prepreprev, preprev, prev, i, n) = 
			if floor(i) = floor(n) then prev+preprev+prepreprev
			else iter_fast(preprev, prev, prev+preprev+prepreprev, i+1.0, n)
		
		
		in iter_fast(1.0, 2.0, 4.0, 4.0, n)
		end;

(*fun FromTo(a,b)=
	if a>b then []
	else a::FromTo(a+1, b);

fun check_all(ls)=
	let fun iterr(p, i) =

	in iterr(ls, 0)
	end;
	frog(x)=frog_fast(x);
	


fun check_eq(a)=
	frog(a)=frog_fast(a);

*)
(*
fun FromTo(a,b)=
	if a>b then []
	else a::FromTo(a+1, b);

fun faster_frog(n)=
	val ls= FromTo(1,n)
	List.nth(ls, 0) = 1
	List.nth(ls, 1) = 2
	List.nth(ls, 2) = 4
	let 
		fun iterr(lis, p, n) =
			if p=n-1 then tl lis
			else
			List.nth(lis, p) =  List.nth(lis, p-1)+List.nth(lis, p-2)+List.nth(lis, p-3)
			iterr(lis, p+1, n)
	in iterr(ls, 0, n)
	end;
*)