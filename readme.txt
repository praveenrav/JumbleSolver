Name: Praveen Ravishankar
Function: Jumble Solver
Date of Last Revision: 08/14/2021

### Calculating Complexity:

Variables:
m - Length of English Dictionary list
k - Length of longest branch in Trie (which is equal to the length of the longest word in the English dictionary list)
n - Length of input string
p - Number of valid English words in given input string

# Time Complexity:

For the main method, the time complexity in the WORST-CASE scenario can be calculated by summing the time complexity of
all the operations performed, which is as follows:

O(1 + 1 + m + m + x + p) ≈ O(x + m + p)

If n ≤ k: x = n!
If n > k: x = n!/(n-k)!

If the given word list can be assumed to be a constant, then the time complexity analysis can be further reduced to:
O(x + p)

# Space Complexity:

Similar to the calculations of the time complexity, the space complexity in the WORST-CASE scenario for the main method
can be calculated by summing the space complexities of all the operations performed, which is as follows:

O(1 + 1 + m + m + y + p + 1) ≈ O(n + m + p)

If the given word list can be assumed to be a constant, then the space complexity analysis can be further reduced to:
O(n + p)

For both the time and space complexities, the values of p in the WORST-CASE are as follows:

If n ≤ k: p = ∑((n!)/((n-i)!)) from i = 0 to i = n
If n > k: p = [∑((n!)/((n-i)!)) (from i = 0 to i = n)] - [∑((n!)/((n-i)!)) (from i = 0 to i = (k - 1))]

The above values of p represent all possible subsets {from size n to size 0} and from {size n to size k} and permutations
of those subsets if {n ≤ k} and if {n > k}, respectively. Additionally, it's important to note that p CANNOT be more
than m, because the number of valid English dictionary word entries cannot exceed the number of valid English dictionary
words.


### Time Complexity Analysis Discussion:
The time complexity calculations above represent the worst-case scenario, as stated previously. However, the calculation
of x is correct if all of the accessed branches of the tree are equal to "k", the length of the longest branch in the
Trie. However, due to the structure of the Trie, not all of the longest branches are equal to "k". As a result, in the
AVERAGE-CASE scenario, the value of "x" would most likely be smaller than the value calculated using the formula above.
In the best-case scenario, the value of "x" would equal "n" since each character in the string would not lead to nested
word/prefix DFS searches.


### Time AND Space Complexity Analyses Discussion:
The value of "p" in the worst-case scenario represents the set of all possible permutations of the subsets of the given
string. Since the number of valid English dictionary words in the given string will most likely be less than the total
number of subsets that can be produced by the spring, it can then be stated that in both the {n ≤ k} and {n > k} cases,
the true value of p in the AVERAGE-CASE scenario will be less than the value of p calculated for the worst-case scenario.
In the best-case scenario, the value of p would equal 0, which corresponds to no matches in the given English dictionary
list.

Although the time and space complexities with using the Trie data structure is high due to the "n!" term, if n is
greater than m, then as n increases, the restrictions imposed on the input string by the Trie structure would be more
and more positively impactful on the speed of the program with respect to n, the length of the input string.

