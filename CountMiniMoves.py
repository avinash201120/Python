def countMinimumMoves(arr, n, k) :

	
	for i in range(k - 1, n) :
		if (arr[i] != arr[k - 1]) :
			return -1

	
	for i in range(k - 1, -1, -1) :
		if (arr[i] != arr[k - 1]) :
			return i + 1

	
	return 0


if __name__ == "__main__" :

	k=int(input())
	arr = list(map(int, input().split()))
	
	n = len(arr)


	print(countMinimumMoves(arr, n, k))


