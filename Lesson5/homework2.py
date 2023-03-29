def min_party_support(group_sizes):

    n = len(group_sizes)

    min_votes = (n // 2) + 1
    max_votes = sum((g + 1) // 2 for g in group_sizes)

    lo, hi = 0, max_votes
    while lo < hi:
        mid = (lo + hi) // 2

        votes_for = 0
        for g in group_sizes:
            votes_for += (g // 2) + min(g % 2, max(0, mid - (g // 2)))
        if votes_for >= min_votes:
            hi = mid
        else:
            lo = mid + 1
    return lo

n = int(input())
group_sizes = list(map, input().split())