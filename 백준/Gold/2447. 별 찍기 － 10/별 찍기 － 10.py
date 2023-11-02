n = int(input())

pattern = [[' ' for _ in range(n)] for _ in range(n)]

def star_recursive(size, x, y):
    if size == 1:
        pattern[x][y] = '*'
        return

    next_size = size // 3

    for dx in range(3):
        for dy in range(3):
            if not(dx == 1 and dy == 1):
                star_recursive(next_size, x + (next_size * dx), y + (next_size * dy))


star_recursive(n, 0, 0)

for p in pattern:
    print(''.join(p))