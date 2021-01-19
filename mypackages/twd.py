# -*- coding: utf-8 -*-

def getConcept(data, decAtr, target):
    #X = {Intervention='yes'}
    if data[decAtr].dtype == "int64":
        X = data[data[decAtr] == int(target)]
    else: 
        X = data[data[decAtr] == target]
    return X.index.tolist()

def getIND(data, col):
    # dataset with conditional attributes
    subdata = data[col]
    
    # dealing with duplicated values
    duplicatedata = subdata[subdata.duplicated(keep=False)]
    ind = duplicatedata.groupby(duplicatedata.columns.values.tolist()).apply(lambda x: list(x.index)).tolist()
    
    dt = data.drop_duplicates(col, keep = False, inplace = False) 
    
    for i in dt.index:
        ind.append(i)
    
    return ind
    
def getProbability(data, ind, X):
    p = {}
    for n in X:
        for m in ind:
            if n == m:
               p[n] = 1
               break
            elif isinstance(m, list) and n in m:
                for k in m:
                    p[k]=1/len(m)
                break
    for i in range(0,data.shape[0]):
        if i not in p.keys():
            p[i] = 0
    return p

def getTWD(alpha, beta, p):
    POS = []
    NEG = []
    BND = []
    for k in p:
        if p[k] >= alpha:
            POS.append(k)
        elif p[k] <= beta:
            NEG.append(k)
        else:
            BND.append(k)
    return POS, NEG, BND

        
    