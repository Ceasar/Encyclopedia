
================================================================================
Optimization Problem
================================================================================

An optimization problem is the problem of finding the best solution from all
feasible solutions.

Dynamic Programming
================================================================================

Dynamic programming is a method for solving complex problems by breaking them
down into simpler subproblems and combining the solutions.

When applicable, dynamic programming takes far less time than naive methods that
do not take advantage of the subproblem overlap (like depth-first search).

Dynamic programming is applicable to problems exhibiting the properties of:
    
1.  Overlapping subproblems

    Overlapping subproblems means that the space of subproblems must be small;
    any recursive algorithm solving the problem should solve the same
    subproblems over and over, rather than generating new subproblems.

    If a problem can be solved by combining optimal solutions to non-overlapping
    subproblems, the strategy is called "divide and conquer" instead. 

2.  Optimal substructure

    Optimal substructure means that the solution to a given optimization problem
    can be obtained by the combination of optimal solutions to its subproblems. 

    Consequently, the first step towards devising a dynamic programming solution
    is to check whether the problem exhibits such optimal substructure.

    A problem that can be broken down recursively is said to have optimal
    substructure.

When developing a dynamic-programming algorithms, we follow a sequence of four
steps:

1. Characterize the structure of an optimal solution

2. Recursively define the value of an optimal solution

3. Compute the value of an optimal solution, typically in a bottom-up fashion

4. Construct an optimal solution from computed information

Steps 1-3 form the basis of a dynamic programming solution to a problem.

If we need only the value of an optimal solution, and not the solution itself,
then we can omit step 4.

Subproblem graphs
================================================================================

When we think about a dynamic-programming problem, we should understand the set
of subproblems involved and how subproblems depend on one another.

The subproblem graph for the problem embodies exactly this information.

Top-down approach
================================================================================

We can view the top-down method (with memoization) for dynamic programming as a
'depth-first search' of the subproblem graph.

Bottom-up approach
================================================================================

The bottom-up method for dynamic programming considers the vertices of the
subproblem graph in such an order that we solve the subproblems `y` adjacent to
a given subproblem `x` before we solve subproblem `x`.

In a bottom-up dynamic programming algorithm, we consider the vertices of the
subproblem graph in an order that is a 'reverse topological sort' or a
'topological sort of the transpose' of the subproblem graph. In other words, no
subproblem is considered until all of the subproblems it depends upon have been
solved.

The size of the subproblem graph G = (V, E) can help us determine the running
time of the dynamic programming algorithm. Since we solve each subproblem just
once, the running time is the sum of the times needed to solve each subproblem.
Typically, the time to compute the solution to a subproblem is proportional to
the degree (number of outgoing edges) of the corresponding vertex in the
subproblem graph, and the number of subproblems is equal to the number of
vertices in the subproblem graph.

Reconstructing a solution
================================================================================

We can extend the dynamic-programming approach to record not only the optimal
value computed for each subproblem, but also a choice that led to the optimal
value.


.. code::

    import functools

    INFINITY = float('inf')

    def memoize(func):
        cache = {}

        @functools.wraps(func)
        def memoized(*args):
            try:
                return cache[args]
            except KeyError:
                cache[args] = func(*args)
                return cache[args]
        return memoized


    def cut_rod1(p, n):
        """Given a rod of length `n` and a table of prices `p`, determine the
        maximum revenue obtainable by cutting up the rod and selling the pieces.

        >>> p = {1: 1, 2: 5, 3: 4, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20, 9: 24, 10: 30}
        >>> cut_rod1(p, 0)
        0
        >>> cut_rod1(p, 1)
        1
        >>> cut_rod1(p, 4)
        10
        >>> cut_rod1(p, 10)
        30
        """
        if n == 0:
            return 0
        q = -INFINITY
        for i in range(1, n + 1):
            if i in p:
                q = max(q, p[i] + cut_rod1(p, n - i))
        return q


    def cut_rod2(p, n):
        def gen_values(n):
            if n == 0:
                yield 0, 0
            else:
                if n in p:
                    yield n, p[n]
                for length, price in gen_values(n - 1):
                    pass
        return max(gen_values(n))

    def cut_rod3(p, n):
        """
        >>> p = {1: 1, 2: 5, 3: 4, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20, 9: 24, 10: 30}
        >>> cut_rod3(p, 0)
        0
        >>> cut_rod3(p, 1)
        1
        >>> cut_rod3(p, 4)
        10
        >>> cut_rod3(p, 10)
        30
        >>> cut_rod3(p, 40)
        120
        """
        r = {0: 0}
        s = {}
        for i in range(1, n + 1):
            q = -INFINITY
            for j in range(1, i + 1):
                if j in p:
                    if q < p[j] + r[i - j]:
                        q = p[j] + r[i - j]
                        s[i] = j
            r[i] = q
        return r[n]


    def hanoi(r, d):
        pass


    def longest_increasing_subsequence(s):
        """Find a subsequence `t` of `s` in which `t`'s elements are in sorted
        order and in which the subsequence is as long as possible.

        >>> longest_increasing_subsequence([2, 4, 3])
        2
        >>> longest_increasing_subsequence([1, 5, 6, 4, 2, 3])
        3
        >>> s = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        >>> longest_increasing_subsequence(s)
        6
        """
        k = max(s)
        a = [0] * k
        b = [INFINITY] * k
        for n in reversed(s):
            print "n:", n
            try:
                q = max(a[n:])
            except ValueError:
                q = 0
            for i in range(k):
                if n < b[i]:
                    b[i] = n
                    a[i] = 1 + q
                if 1 + q >= a[i] and n < b[i]:
                    b[i] = n
                    a[i] = 1 + q
            print a
            print b
        return max(a)

        """
        def gen_seqs(s):
            if len(s) == 0:
                pass
            elif len(s) == 1:
                yield s
            else:
                seen = set()
                for seq in gen_seqs(s[1:]):
                    if tuple(seq) in seen:
                        continue
                    else:
                        seen.add(tuple(seq))

                    yield seq

                    if s[0] < seq[0]:
                        yield [s[0]] + seq
                    elif s[0] > seq[0]:
                        yield [s[0]]
        return len(max(gen_seqs(s), key=lambda xs: len(xs)))
