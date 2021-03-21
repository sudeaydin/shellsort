a=[54,26,93,17,77,31,44,55,20,12,40,88]
N=12
stepsize=3
h=int(N/stepsize)
h=int(h)
while h>=1:
    for i in range(h,N):
        j=i
        while j>=h and a[j]<a[j-h]:
            a[j],a[j-h]=a[j-h],a[j]
            j=j-h
    h=int(h/stepsize)
print(a)    
