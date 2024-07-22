N = 100 
A.<a,b>=PolynomialRing(QQ)
R.<q> = PowerSeriesRing(A,default_prec=N)
QM = QuasiModularForms(1)
E2 = QM.0.q_expansion(N)
E4 = R(ModularForms(1,4).basis()[0].q_expansion(N))
E6 = R(ModularForms(1,6).basis()[0].q_expansion(N))
eta = sage.modular.etaproducts.qexp_eta(R, N)
p=3

E2s = E2 - p * E2(q^p)
E4s = E4 - p^(3) * E4(q^p)  
E6s = E6 - p^(5) * E6(q^p)

h=q*(eta((q^p))/eta)^((24/(p-1)))
h=R(h.truncate(N))


n=1
m =1
K=4


Ek = R(ModularForms(1,K).basis()[0].q_expansion(N))


hmterm1full = h^(n) * (Ek - p^(K) * Ek(q^(p)))^(3*p^m)
hmterm2full = (h^(-n)) * (Ek(q^(p)) - Ek)^(3*p^m)
hmterm1 = sum([hmterm1full[i] * q^(i) for i in range(0,floor(N/2)-1)])
hmterm2 = sum([hmterm2full[p * i] * q^(i) for i in range(-p, floor(N/p)-1)])
hm = hmterm1 + p^(1-((12*n)/(p-1)))* hmterm2

weight =  3*K * p^(m)

hmder = q * derivative(hm,q) - (weight/12) * E2 * hm
hmder2 = q * derivative(hmder,q) - ((weight + 2) / 12) * E2 * hmder
hmder3 = q * derivative(hmder2,q) - ((weight + 4)/ 12) * E2 * hmder2
hmder4 = q * derivative(hmder3,q) -((weight + 6)/12) * E2 * hmder3
hmder5 = q * derivative(hmder4,q) - ((weight + 8)/12) * E2 * hmder4

M=Matrix([[xx[ii] for xx in [hm*E4^2,hm*E2s^2*E4,hm*E2s*E6,
                             hmder*E6,hmder*E4*E2s,hmder*E2s^3,
                             hmder2*E4,hmder2*E2s^2,hmder3*E2s,hmder4]] for ii in range(30)])
show(M.rref())

#M=Matrix([[xx[ii] for xx in [hm*E6,hm*E4*E2s,hm*E2s^3,
                   #         hmder*E4,hmder*E2s^2,hmder2*E2s,hmder3]] for ii in range(30)])
#show(M.rref())

#M=Matrix([[xx[ii] for xx in [hm*E2s^5,hm*E2s^3*E4,hm*E2s^2*E6,hm*E4^2*E2s,
   #                         hmder*E2s^4,hmder*E2s^2*E4,hmder*E2s*E6,hmder*E4^2,
  #                        hmder2*E2s^3,hmder2*E4*E2s,hmder2*E6,hmder3*E4,hmder4*E2s,hmder5]] for ii in range(30)])
#show(M.rref())
