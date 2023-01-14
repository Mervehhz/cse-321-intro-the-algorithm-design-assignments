def find_winner_dc(n: int, k: int) -> int:
    if n == 2:
        return 2 if k == 1 else 1
    survivor_position_in_subgroup = find_winner_dc(n - n // 2, k)
    if survivor_position_in_subgroup > n // 2:
        return (survivor_position_in_subgroup - 1) * 2
    else:
        return survivor_position_in_subgroup * 2 - 1
    

print(find_winner_dc(24,1))