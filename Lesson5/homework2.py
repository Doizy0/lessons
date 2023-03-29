def can_pass_decision(num_supporters, group_sizes):
    num_groups = len(group_sizes)
    num_yes_votes = 0
    for group_size in group_sizes:
        num_yes_votes += min(num_supporters, (group_size + 1) // 2)
        if num_yes_votes > num_supporters:
            return False
    return num_yes_votes > num_groups // 2


num_groups = int(input())
group_sizes = list(map(int, input().split()))


lo, hi = 0, sum(group_sizes)
while lo < hi:
    mid = (lo + hi) // 2
    if can_pass_decision(mid, group_sizes):
        hi = mid
    else:
        lo = mid + 1


print(lo)
