s = input()
q = list(map(str,s.split()))
j = list()
k = ''
for i in s.split():
    for a in i:
        if a.isdigit():
            k+=a
    j.append(int(k))
    k = ''
for i in range(len(j)):
    for a in range(i+1,len(j)):
        if j[i]>j[a]:
            j[i],j[a] = j[a],j[i]
            q[i],q[a] = q[a],q[i]
s = ''
for i in q:
    for a in i:
        if not(a.isdigit()):
            s+=a
    s+=' '
print(s.strip())