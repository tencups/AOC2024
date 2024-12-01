
from collections import Counter 
l = []
r = []


with open("input.txt", "r") as file:
    for line in file:
        numbers = line.strip().split()

        l.append(int(numbers[0]))
        r.append(int(numbers[1]))


def distances_PART1(l, r):


    l.sort()
    r.sort()
    dist = 0

    for num1, num2 in zip(l, r):
        dist += abs(num1 - num2)
    return dist

def similarity_PART2(l, r):

    l.sort()
    r.sort()
    sim = 0

    right_map = Counter(r)

    for num in l:
        sim += (num * right_map[num])
    
    return sim

print(distances_PART1(l, r))
print(similarity_PART2(l, r ))