def lds(arr, n):
    lds = [0] * n
    max = 0
    for i in range(n):
        lds[i] = 1
        
    for i in range(1, n):
        for j in range(i):
            if (arr[i] < arr[j] and lds[i] < lds[j] + 1):
                lds[i] = lds[j] + 1
        for i in range(n):
            if (max < lds[i]):
                max = lds[i]
    return max


if __name__ == "__main__":
    
    a=int(input())
    arr=list(map(int,input().strip().split()))[:a]
    n = len(arr)
    print(lds(arr, n))


