
def gale_shapley(n, men_prefs, women_prefs):
    # Initialize all men and women as free
    free_men = set(range(n))
    free_women = set(range(n))

    pairs = {}

    while free_men:
        print("List of free men: ", free_men)
        print("List of free women: ", free_women)
        man = free_men.pop()
        man_prefs = men_prefs[man]
        print("Preferences of Man #", man, ": ", man_prefs)
        woman = man_prefs.pop(0)
        print(men_prefs)
        print("The woman: ", woman)

        if woman in free_women:
            # If the woman is free, pair the man and woman
            pairs[man] = woman  # pairs.update({man:woman})
            free_women.remove(woman)
        else:
            # If the woman is not free, check if the man is preferred over the
            # current partner
            current_partner = list(pairs.keys())[list(pairs.values()).index(woman)]
            woman_prefs = women_prefs[woman]
            if woman_prefs.index(man) < woman_prefs.index(current_partner):
                # If the man is preferred, pair the man and woman and make the
                # current partner free
                pairs.update({man:woman})
                del pairs[current_partner]
                free_men.add(current_partner)
                free_men = set(list(free_men))
            else:
                free_men.add(man)
                free_men = set(list(free_men))
        print(pairs)
    return pairs


''' 
4 men and 4 women, and the preferences:
Man 0: Woman 3, Woman 2, Woman 1, Woman 0
Man 1: Woman 0, Woman 1, Woman 2, Woman 3
Man 2: Woman 1, Woman 0, Woman 3, Woman 2
Man 3: Woman 2, Woman 3, Woman 0, Woman 1
Woman 0: Man 1, Man 0, Man 3, Man 2
Woman 1: Man 2, Man 0, Man 1, Man 3
Woman 2: Man 3, Man 0, Man 2, Man 1
Woman 3: Man 0, Man 1, Man 2, Man 3
'''

n = 4
# men_prefs = {
#     0: [0, 2, 1, 3],
#     1: [0, 1, 2, 3],
#     2: [1, 0, 3, 2],
#     3: [2, 0, 1, 3],
# }
# women_prefs = {
#     0: [1, 0, 3, 2],
#     1: [2, 0, 1, 3],
#     2: [3, 0, 2, 1],
#     3: [0, 1, 2, 3],
# }
men_prefs = {
    0: [0, 2, 1, 3],
    1: [0, 2, 1, 3],
    2: [0, 2, 1, 3],
    3: [0, 2, 1, 3],
}
women_prefs = {
    0: [1, 0, 3, 2],
    1: [1, 0, 3, 2],
    2: [1, 0, 3, 2],
    3: [1, 0, 3, 2],
}

pairs = gale_shapley(n, men_prefs, women_prefs)