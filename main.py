n = int(input())
for row in range(1, n+1):
    space = " " * (n - row)
    stars = "*" * row
    print(space + stars)
