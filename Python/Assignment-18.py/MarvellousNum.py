def ChkPrime(n,lst):
    primelst=[]
    for i in range(len(lst)):
        for j in range(lst[i]):
            if (lst[i]%i)



    for i in range(2,len(lst)):
        if(lst[i]%i != 0):
            primelst.append(lst[i])
            break
    primesum=0
    for i in range(len(primelst)):
        primesum=primesum+primelst[i]
    return primesum

        

                
