

# %% FIBONACCI
# Naive fibonacci equation with O(2^n) time complexity (can be seen by drawing a tree - two calls made for every call).
def fibNaive(n):
	if n == 1 or n == 2: return 1
	return calcFib(n-1) + calcFib(n-2)


# Improved fibonacci equation with O(n) time complexity using memoisation
def calcFib(n, memo={}):  # Default argument must be mutable: only defined once
	if n in memo: return memo[n]
	if n == 1 or n == 2: return 1
	memo[n] = calcFib(n-1, memo) + calcFib(n-2, memo)
	return memo[n]


# Attempt at tabulating a fibonacci function (putting into a table)
# Tabulation handles problems iteratively instead of recursively (bottom-up)... still kind of a brute force
def fibTabulation(n):
	# Fill in base cases of table
	tab = [0, 1]

	for i in range(2, n+1):
		tab.append(tab[i-1] + tab[i-2])
	return tab[n]

def initialise(n):
	# Fill in base cases of table
	tab = [0] * (n+1)
	tab[:2] = 0, 1

	for i in range(2, n+1):
		tab[i] = tab[i-1] + tab[i-2]
	return tab[n]

print(initialise(20))
