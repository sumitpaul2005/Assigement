for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i][1] > lis[j][1]:
            lis[i], lis[j] = lis[j] , lis[i]