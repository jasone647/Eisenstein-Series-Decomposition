#!/usr/bin/env python
# coding: utf-8

# In[1]:


p=5
N=70
R.<q> = PowerSeriesRing(QQ)

E2 = 1-24*sum([sigma(n)*q^n for n in range(1,N+1)])
E4 = 1+240*sum([sigma(n,3)*q^n for n in range(1,N+1)])
E6 = 1-504*sum([sigma(n,5)*q^n for n in range(1,N+1)])


E2s=E2-p^(2-1)*E2(q^p)
E4s=E4-p^(4-1)*E4(q^p)
E6s=E6-p^(6-1)*E6(q^p)

def D(f,k):
    return q*f.derivative(q)-(k/12)*E2*f

h=q*prod([1-q^(p*n) for n in range(1,N)])^(24/(p-1))/prod([1-q^(n) for n in range(1,floor(N))])^(24/(p-1))
h=R(h.truncate(N))
n=2
hn = h^n

hp=D(hn,0)
htwo=D(hp,2)
hthree=D(htwo,4)
hfour=D(hthree,6)
hfive = D(hfour,8)

W2 = [E2s]  
W4 = [E2s^2,E4,E4s]  
W6 = [E2s^3,E2s*E4,E2s*E4s]  
W8 = [E2s^4,E2s^2*E4,E2s^2*E4s,E4^2,E4s^2,]  
W10=[E2s^5,E2s*E4^2,E2s*E4s^2,E2s^3*E4,E2s^3*E4s]  

hs = []
hfour12 = [hfour*i for i in W2]
for i in hfour12:
    hs.append(i)
hthree12 = [hthree*i for i in W4]
for i in hthree12:
    hs.append(i)
htwo12 = [htwo*i for i in W6]
for i in htwo12:
    hs.append(i)
hone12 = [hp*i for i in W8]
for i in hone12:
    hs.append(i)
h12 = [hn*i for i in W10]
for i in h12:
    hs.append(i)
hs.append(hfive)


M=Matrix([[xx[ii] for xx in hs] for ii in range(23)])
show(M.rref())


# In[ ]:




