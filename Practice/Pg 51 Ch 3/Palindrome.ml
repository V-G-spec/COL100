fun rev(n)=
       let fun it(n,c)=
               if n=0 then c
               else it(n div 10, (c*10)+ (n mod 10))
       in it(n,0)
end;

fun palin(n)=(n=rev(n));