# The Levenshtein distance refers to the minimum number of operations required to transform one string into another
# Operations: Removal, insertion, deletion
# In theory you can solve this dynamically...

# Memoised attempt at Levenshtein distance problem
def levenshteinDistance(first: str, second: str, memo={}) -> int:
	# Check if target in memo
	key = (first, second)
	if key in memo: return memo[key]

	# Base cases
	if first == second: return 0  # If strings are the same, return 0
	if first == "" or second == "": return len(first) + len(second)  # If either empty, count == removing all chars in other string

	# If strings are different, compare first letters
	if first[:1] == second[:1]:
		memo[(first, second)] = levenshteinDistance(first[1:], second[1:])
		return memo[key]
	else:
		memo[key] = min(levenshteinDistance(first[1:], second[1:]),
						levenshteinDistance(first, second[1:]),
						levenshteinDistance(first[1:], second)) + 1
		return memo[key]


first = "a"
second = "a"
print(levenshteinDistance(first, second))

