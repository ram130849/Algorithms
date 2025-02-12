def longestPalindromeSubseq(s:str)-> int:
    n = len(s)
    row = [0 for i in range(n)]
    dp_mat = [row for j in range(n)]
    # Storing length of diagonal values. since each character is a palindrom of length 1.
    for i in range(n):
        dp_mat[i][i] = 1
    # Loop through the dp matrix.
    for k in range(2, n+1):
        for i in range(n-k+1):
            j = i+k-1
            # when characters are equal and length is 2. we increment dp matrix by 2.
            if(s[i] == s[j] and k == 2):
                dp_mat[i][j] = 2
            # when characters are equal and length is greater than 2. we increment next row and previous column dp value by 2.
            elif(s[i] == s[j]):
                dp_mat[i][j] = dp_mat[i+1][j-1]+2
            # else we take maximum of previous column dp value or next row dp value.
            else:
                dp_mat[i][j] = max(dp_mat[i][j-1], dp_mat[i+1][j]) 

    return dp_mat[0][n-1]

def CondensedIntegers(k, factors):
    integers = [1]
    indices = [0]*len(factors)
    fact_index = {}
    k_condensed_integers = [-1]*k
    k_condensed_integers[0] = 1
    
    # getting the indexes of the factors.
    for i in range(len(factors)):
        fact_index[factors[i]] = i

    # looping through for the first k integers.
    for i in range(1,k):
        min_val = float('inf')
        # getting the minimum indexed factor values.
        for j in range(len(factors)):
            val = factors[j]*(k_condensed_integers[indices[j]])
            if(val<min_val):
                min_val = val
        k_condensed_integers[i] = min_val
        # updating the indexes based on the minimum indexed factor values.
        for j in range(len(factors)):
            val = factors[j]*(k_condensed_integers[indices[j]])
            if(val==min_val):
                indices[j]+=1
        # adding the min factors to the resultant array.
        integers.append(min_val)
    return integers

def tower_rouge(tower):
    m,n = len(tower),len(tower[0])
    row = [0 for _ in range(n+1)]
    dp_mat = [row for _ in range(m+1)]

    if(tower[m-1][n-1]>0):
        dp_mat[m-1][n-1] = 1
    else:
        dp_mat[m-1][n-1] = abs(tower[m-1][n-1])+1
    
    # fixing the column to the last index and checking the 
    for i in range(m-2,-1,-1):
        dp_mat[i][n-1] = max(dp_mat[i+1][n-1]-tower[i][n-1],1)
    
    # fixing the row to the last index and checking the    
    for j in range(n-2,-1,-1):
        dp_mat[m-1][j] = max(dp_mat[m-1][j+1]-tower[m-1][j],1)
    
    # Looping through the rows and columns backwards and 
    # finding the minimum possible energy to backtracking to the initial state.
    for i in range(m-2,-1,-1):
        for j in range(n-2,-1,-1):
            mp_exit = min(dp_mat[i+1][j],dp_mat[i][j+1])
            dp_mat[i][j] = max(mp_exit - tower[i][j],1)

    # returning the initial value.
    return dp_mat[0][0]

def find_median(arr1,arr2,target):
    i,j = len(arr1),len(arr2)

    if(i<=0):
        return arr2[target-1]

    if(j<=0):
        return arr1[target-1]

    med_a,med_b = i//2+1,j//2+1
    ma,mb = arr1[i//2],arr2[j//2]
    # if the median indexes are greater than the current target index we check 
    # on the target index with half of the array based on the array values.
    if((med_a+med_b)>target):
        if(ma>mb):
            return find_median(arr1[:med_a-1],arr2,target)
        else:
            return find_median(arr1,arr2[:med_b-1],target)
    # if the median indexes are lesser than the current target index we check on the remaining
    # target index with half of the array based on the array values.
    else:
        if(ma>mb):
            return find_median(arr1,arr2[med_b:],target-med_b)
        else:
            return find_median(arr1[med_a:],arr2,target-med_a)

def getMedian(arr1,arr2,n):
    median = 0
    i,j = len(arr1),len(arr2)
    if(i!=j):
        return -1
    # if the length of the first array is 0 then median value is found in the second array 
    if(i==0):
        if(j%2==0):
            return (arr2[j//2 -1] + arr2[j//2])/2
        else:
            return (arr2[j//2])

    # if the length of the second array is 0 then median value is found in the first array.
    if(j==0):
        if(i%2==0):
            return (arr1[i//2-1] + arr1[i//2])
        else:
            return (arr1[i//2])

    # if the length of the arrays are even, 
    # then median for both the arrays are found in the array.        
    if((i+j)%2==0):
        return (find_median(arr1,arr2,(i+j)//2) + find_median(arr1,arr2,((i+j)//2)+1))/2

    return find_median(arr1,arr2,(i+j)//2+1)

def no_of_ways(n:int):
    if(n%2!=0):
        return 0
    A = [0]*(n+1)
    B = [0]*(n+1)
    A[0] = 1 
    A[1] = 0
    B[0] = 0
    B[1] = 1
    # Looping for the remaining integers values.
    for i in range(2,n+1):
        A[i] = A[i-2] + 2*(B[i-1])
        B[i] = A[i-1] + B[i-2]
    return A[n]



































