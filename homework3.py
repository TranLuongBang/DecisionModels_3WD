# -*- coding: utf-8 -*-
from mypackages import twd
import pandas as pd

def main():
    
    print('Input data filename:')
    filename = input()
    data = pd.read_csv(filename)
    print(data)
    print(data.columns.tolist())
    
    
    print('Input decision attribute:')
    decAtr = input() 
    
    print('Input decision value:')
    target = input()
    x = twd.getConcept(data, decAtr, target)
    print('The concept X:', x)
    print('There are ', len(x), ' patients having diabetes')
    print('There are ', data.shape[0]-len(x), ' patients not having diabetes')
    
    print('Input conditional attributes:')
    col = input().split()
    ind = twd.getIND(data, col)
    print('Indiscernibility relation IND:', ind)
    
    
    print('Conditional probability of Objects in concept:')
    p = twd.getProbability(data, ind, x)
    print(p)
    
    print('Input alpha threshold:')
    alpha = float(input())
    
    print('Input beta threshold:')
    beta = float(input())
    
    output = twd.getTWD(alpha, beta, p)
    
    print('The positive regions of three-way decisions')
    print("POS = ", output[0])
    print("Accept number of patients having diabetes:", len(output[0]))
    
    print('The negative regions of three-way decisions')
    print("NEG = ", output[1])
    print("Reject number of patients having diabetes:", len(output[1]))
    
    print('The boundary regions of three-way decisions')
    print("BND = ", output[2])
    print("Noncommitment number of patients having diabetes:", len(output[2]))
main()