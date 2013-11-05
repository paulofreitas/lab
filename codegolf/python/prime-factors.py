x=raw_input();n=int(x);f=[];c=f.count;d=2
while n>1:
 while n%d==0:f+=[d];n/=d
 d+=1
print x+':',' '.join((`n`,`n`+'^'+`c(n)`)[c(n)>1]for n in sorted(set(f)))