# store file input into 2D list
reports = []
with open("input.txt", "r") as file:
    for line in file:
        levels = line.strip().split()
        levels = [int(elt) for elt in levels]
        reports.append(levels)

def is_safe(report):
        
    inc = 1
    dec = 1
    # check increasing
    for idx in range(0, len(report)-1):
        if 1 <= report[idx] - report[idx+1] <=3:
            continue
        else:
            inc = 0
            break
    
    #check decreasing
    for idx in range(0, len(report)-1):
        if 1 <= report[idx+1] - report[idx] <=3:
            continue
        else:
            dec = 0
            break

    return inc + dec


def safe_count_PART1(reports):

    count = 0
    for report in reports:
        count += is_safe(report)

    return count


def safe_count_dampen_PART2(reports):
    count = 0

    for report in reports:
        if is_safe(report):
            count +=1
        else: # check if we can tolerate single bad level
            for i, level in enumerate(report):
                copy = report.copy()
                del copy[i]
                if is_safe(copy): # stop checking after the "single bad level" is found
                    count+=1
                    break
    
    return count
        



print(safe_count_PART1(reports))
print(safe_count_dampen_PART2(reports))

