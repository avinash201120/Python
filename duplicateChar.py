from collections import defaultdict

def printDups(st):

	count = defaultdict(int)
	for i in range(len(st)):
		count[st[i]] += 1

	for it in count:
		if (count[it] > 1):
			print(it, "-", count[it])

if __name__ == "__main__":

	st = input("")
	printDups(st)

