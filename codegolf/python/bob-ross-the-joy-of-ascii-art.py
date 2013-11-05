import sys;o={}
for l in sys.stdin:x,y,c=map(int,l[:-1].split());o[y]=o.get(y,{});o[y][x]=chr(c)
for n in o:print''.join(o[n].get(i,' ')for i in range(max(o[n])+1))