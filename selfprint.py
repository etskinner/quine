s="""
s=___
t=s.splitlines()
u=t[1].replace("_",'"')
print(u,end="")
print(s)
v=t[-2].replace("_",'"')
print(v)
for i in t[2:-2]:
    print(i)
___
"""
t=s.splitlines()
u=t[1].replace("_",'"')
print(u,end="")
print(s)
v=t[-1].replace("_",'"')
print(v)
for i in t[2:-1]:
    print(i)
