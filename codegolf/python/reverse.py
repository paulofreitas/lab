n=map(int,raw_input().split());f=0;l=len(n)
while n!=sorted(n):
 m=n.index(max(n[:l-f]))+1
 if m==1:m=l-f;f+=1
 n=n[:m][::-1]+n[m:];print m,