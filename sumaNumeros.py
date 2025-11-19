def get_sum(a,b):
    if a == b:
        return a
    m, M = min(a, b), max(a, b)
    return (M - m + 1) * (m + M) // 2