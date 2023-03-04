from itertools import permutations


string = input()



def our_permutations(string):

    combs = list(permutations(string))

    words = []

    for comb in combs:
        words.append(''.join(comb))
    return words


print(*our_permutations(string), sep='\n')