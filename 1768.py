n = int(input())
rows = (n // 2) + 1
row_spaces = n // 2
row_stars = 1
for row in range(rows):
    line = (" " * row_spaces) + ('*' * row_stars)
    print(line)

    row_stars += 1
    row_spaces += 1


print()