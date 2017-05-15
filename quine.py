s="""
s=___
t=s.splitlines()
u=t[1].replace("_",'"')
print(u,end="")
print(s[:-1])
v=t[-1].replace("_",'"')
print(v)
for i in t[2:-1]:
    print(i)
___
"""
t=s.splitlines()
u=t[1].replace("_",'"')
print(u,end="")
print(s[:-1])
v=t[-1].replace("_",'"')
print(v)
for i in t[2:-1]:
    print(i)
