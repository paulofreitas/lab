def a(x,u):
 r=p=u//x;n=3;s=-1;t=1
 while t:p//=x*x;t=p//n;r+=s*t;s=-s;n+=2
 return r
u=10**1010;print'3.'+`(16*a(5,u)-4*a(239,u))//10**10`[1:-1]