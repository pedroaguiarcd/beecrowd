while True:
    n = int(input())
    if n == 0:
        break
    max_len = 0
    lines = []
    for _ in range(n):
        line = input().strip()
        line_len = 0 #comprimento atual
        prev_len = 1
        while line_len != prev_len:
            prev_len = len(line) #comprimento da ultima
            line = line.replace("  ", " ")
            line_len = len(line)
        if line_len > max_len:
            max_len = line_len

        lines.append(line)

    for line in lines:
        print(line.rjust(max_len))

