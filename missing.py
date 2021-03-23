lists = list(range(1, 100000))
print(lists[80])
print(lists[7895])
print(lists[89])

lists.remove(80)
lists.remove(7895)
lists.remove(89)


def find(tar):
    i = 0
    while i < len(tar) - 1:
        if tar[i] != tar[i + 1] - 1:
            print(f"The missing number is {tar [i + 1]}")
        i += 1


find(lists)
