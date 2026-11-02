dial = 50
k = 0
with open("input.txt") as f:
  for x in f:
    dir = x[0]
    step = int(x[1:])
    dial += step if dir == "R" else -step
    k+=dial//100
    dial %= 100

    if dial < 0:
       dial += 100
       k += 1
    if dial > 99:
        dial -= 100
        k += 1
    print(f"dir {dir} step {step} dial {dial}")
print(k)
