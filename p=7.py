p=7
N=100
R.<q> = PowerSeriesRing(QQ)

#Define Eisenstein series
E2 = 1-24*sum([sigma(n)*q^n for n in range(1,N+1)])
E4 = 1+240*sum([sigma(n,3)*q^n for n in range(1,N+1)])
E6 = 1-504*sum([sigma(n,5)*q^n for n in range(1,N+1)])

E2s=E2-p^(2-1)*E2(q^p)
E4s=E4-p^(4-1)*E4(q^p)
E6s=E6-p^(6-1)*E6(q^p)

#Define modular derivative operation
def D(f,k):
    return q*f.derivative(q)-(k/12)*E2*f

h=q*prod([1-q^(p*n) for n in range(1,N)])^(24/(p-1))/prod([1-q^(n) for n in range(1,floor(N))])^(24/(p-1))
h=R(h.truncate(N))
n=1
hn = h^n

hp=D(hn,0)
htwo=D(hp,2)
hthree=D(htwo,4)
hfour=D(hthree,6)
hfive = D(hfour,8)
hsix = D(hfive,10)
hseven = D(hsix,12)

#Lists of combinations of generators of each weight
W2=[E2,E2s]
W4=[E4,E2*E2,E2s*E2,E2s*E2s]
W6=[E6,E4*E2,E4*E2s,E2*E2*E2,E2s*E2*E2,E2s*E2s*E2,E2s*E2s*E2s]
W8=[E6*E2,E6*E2s,E4*E4,E4*E2*E2,E4*E2s*E2,E4*E2s*E2s,E2*E2*E2*E2,E2s*E2*E2*E2,E2s*E2s*E2*E2,E2s*E2s*E2s*E2,E2s*E2s*E2s*E2s]
W10=[E6*E4,E6*E2*E2,E6*E2s*E2,E4*E4*E2,E6*E2s*E2s,E4*E4*E2s,E4*E2*E2*E2,E4*E2s*E2*E2,E4*E2s*E2s*E2,E4*E2s*E2s*E2s,E2*E2*E2*E2*E2,E2s*E2*E2*E2*E2,E2s*E2s*E2*E2*E2,E2s*E2s*E2s*E2*E2,E2s*E2s*E2s*E2s*E2,E2s*E2s*E2s*E2s*E2s]
W12=[E6*E6,E6*E4*E2,E6*E4*E2s,E4*E4*E4,E6*E2*E2*E2,E6*E2s*E2*E2,E4*E4*E2*E2,E6*E2s*E2s*E2,E4*E4*E2s*E2,E6*E2s*E2s*E2s,E4*E4*E2s*E2s,E4*E2*E2*E2*E2,E4*E2s*E2*E2*E2,E4*E2s*E2s*E2*E2,E4*E2s*E2s*E2s*E2,E4*E2s*E2s*E2s*E2s,E2*E2*E2*E2*E2*E2,E2s*E2*E2*E2*E2*E2,E2s*E2s*E2*E2*E2*E2,E2s*E2s*E2s*E2*E2*E2,E2s*E2s*E2s*E2s*E2*E2,E2s*E2s*E2s*E2s*E2s*E2,E2s*E2s*E2s*E2s*E2s*E2s]
W14=[E6*E6*E2,E6*E6*E2s,E6*E4*E4,E6*E4*E2*E2,E6*E4*E2s*E2,E4*E4*E4*E2,E6*E4*E2s*E2s,E4*E4*E4*E2s,E6*E2*E2*E2*E2,E6*E2s*E2*E2*E2,E4*E4*E2*E2*E2,E6*E2s*E2s*E2*E2,E4*E4*E2s*E2*E2,E6*E2s*E2s*E2s*E2,E4*E4*E2s*E2s*E2,E6*E2s*E2s*E2s*E2s,E4*E4*E2s*E2s*E2s,E4*E2*E2*E2*E2*E2,E4*E2s*E2*E2*E2*E2,E4*E2s*E2s*E2*E2*E2,E4*E2s*E2s*E2s*E2*E2,E4*E2s*E2s*E2s*E2s*E2,E4*E2s*E2s*E2s*E2s*E2s,E2*E2*E2*E2*E2*E2*E2,E2s*E2*E2*E2*E2*E2*E2,E2s*E2s*E2*E2*E2*E2*E2,E2s*E2s*E2s*E2*E2*E2*E2,E2s*E2s*E2s*E2s*E2*E2*E2,E2s*E2s*E2s*E2s*E2s*E2*E2,E2s*E2s*E2s*E2s*E2s*E2s*E2,E2s*E2s*E2s*E2s*E2s*E2s*E2s]

#Multiply modular derivates by elements of appropriate weight to make them weight 14, put them all into list hs to use in matrix
hs = []
hsix12 = [hsix*i for i in W2]
for i in hsix12:
    hs.append(i)
hfive12 = [hfive*i for i in W4]
for i in hfive12:
    hs.append(i)
hfour12 = [hfour*i for i in W6]
for i in hfour12:
    hs.append(i)
hthree12 = [hthree*i for i in W8]
for i in hthree12:
    hs.append(i)
htwo12 = [htwo*i for i in W10]
for i in htwo12:
    hs.append(i)
hone12 = [hp*i for i in W12]
for i in hone12:
    hs.append(i)
hs.append(hseven)
print(len(hs))

M=Matrix([[xx[ii] for xx in hs] for ii in range(65)])
show(M.rref())
