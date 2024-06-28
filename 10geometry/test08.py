lines = list(map(int, input().split()))
if max(lines) < sum(lines) - max(lines):
    print(sum(lines))
else:
    after_max = sum(lines) - max(lines) - 1
    lines[lines.index(max(lines))] = after_max
    print(sum(lines))

