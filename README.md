# stable-marriage-problem-Gale-Shapley
Python Implementation of Gale-Shapley algorithm for Stable Marriage Problem

Gale & Shapley proved that for equal number of men and women, stable marriage or stable one-to-one matching is always possible. This is the pyhton implementation of their algorithm.

Working principle:
1. Take an arbitrary free man
2. Select the best preferred woman for this man who he hasn't proposed yet
3. If the woman is free or prefers this man over her current match, pair the man and woman and free the previous match
4. Repeat until no free man remain
