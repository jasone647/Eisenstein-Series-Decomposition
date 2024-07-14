#Code for Finding combinations of generators of each weight
#Enter Generators and corresponding weights in the following dictionary then run

X = {'Id':0,'E2':2,'E2s':2,'E4':4,'E4s':4,'E6':6,'E6s':6}

W2a,W4a,W6a,W8a,W10a,W12a,W14a = [],[],[],[],[],[],[]
for i in X:
    for j in X:
        for k in X:
            for l in X:
                for m in X:
                    for o in X:
                        for p in X:
                            if X[i]+X[j]+X[k]+X[l]+X[m]+X[o]+X[p]==2:
                                W2a.append([i,j,k,l,m,o,p])

for i in X:
    for j in X:
        for k in X:
            for l in X:
                for m in X:
                    for o in X:
                        for p in X:
                            if X[i]+X[j]+X[k]+X[l]+X[m]+X[o]+X[p]==4:
                                W4a.append([i,j,k,l,m,o,p])
                                                             
for i in X:
    for j in X:
        for k in X:
            for l in X:
                for m in X:
                    for o in X:
                        for p in X:
                            if X[i]+X[j]+X[k]+X[l]+X[m]+X[o]+X[p]==6:
                                W6a.append([i,j,k,l,m,o,p])

for i in X:
    for j in X:
        for k in X:
            for l in X:
                for m in X:
                    for o in X:
                        for p in X:
                            if X[i]+X[j]+X[k]+X[l]+X[m]+X[o]+X[p]==8:
                                W8a.append([i,j,k,l,m,o,p])                                
  
for i in X:
    for j in X:
        for k in X:
            for l in X:
                for m in X:
                    for o in X:
                        for p in X:
                            if X[i]+X[j]+X[k]+X[l]+X[m]+X[o]+X[p]==10:
                                W10a.append([i,j,k,l,m,o,p])                                

for i in X:
    for j in X:
        for k in X:
            for l in X:
                for m in X:
                    for o in X:
                        for p in X:
                            if X[i]+X[j]+X[k]+X[l]+X[m]+X[o]+X[p]==12:
                                W12a.append([i,j,k,l,m,o,p])                                
                                                                
for i in X:
    for j in X:
        for k in X:
            for l in X:
                for m in X:
                    for o in X:
                        for p in X:
                            if X[i]+X[j]+X[k]+X[l]+X[m]+X[o]+X[p]==14:
                                W14a.append([i,j,k,l,m,o,p])                                
                                
                                    
W2b=[]
for i in W2a:
    k = [k for k in i if k!='Id']
    W2b.append(k)
W2 = []
[W2.append(x) for x in W2b if x not in W2]
result = {tuple(sorted(i)): i for i in W2}.values()
print(list(result))


W4b=[]
for i in W4a:
    k = [k for k in i if k!='Id']
    W4b.append(k)
W4 = []
[W4.append(x) for x in W4b if x not in W4]
result = {tuple(sorted(i)): i for i in W4}.values()
print(list(result))

W6b=[]
for i in W6a:
    k = [k for k in i if k!='Id']
    W6b.append(k)
W6 = []
[W6.append(x) for x in W6b if x not in W6]
result = {tuple(sorted(i)): i for i in W6}.values()
print(list(result))

W8b=[]
for i in W8a:
    k = [k for k in i if k!='Id']
    W8b.append(k)
W8 = []
[W8.append(x) for x in W8b if x not in W8]
result = {tuple(sorted(i)): i for i in W8}.values()
print(list(result))

W10b=[]
for i in W10a:
    k = [k for k in i if k!='Id']
    W10b.append(k)
W10 = []
[W10.append(x) for x in W10b if x not in W10]
result = {tuple(sorted(i)): i for i in W10}.values()
print(list(result))

W12b=[]
for i in W12a:
    k = [k for k in i if k!='Id']
    W12b.append(k)
W12 = []
[W12.append(x) for x in W12b if x not in W12]
result = {tuple(sorted(i)): i for i in W12}.values()
print(list(result))
print(len(list(result)))

W14b=[]
for i in W14a:
    k = [k for k in i if k!='Id']
    W14b.append(k)
W14 = []
[W14.append(x) for x in W14b if x not in W14]
result = {tuple(sorted(i)): i for i in W14}.values()
print(list(result))
print(len(list(result)))
