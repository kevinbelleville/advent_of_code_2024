
safe_reports = 0

with open('input_day2.txt', 'r') as file:
    lines = file.readlines()

new_lines = []

for line in lines:
    a = line.strip().split(" ")
    new_lines.append(a)


def is_safe_report(line):
    diffs = []
    prev = 0
    for i in range(len(line)):
        if i == 0:
            prev = int(line[i])
        else:
            diff = int(line[i]) - prev
            diffs.append(diff)
            prev = int(line[i])
    
    could_be_safe = True
    all_neg = True
    all_pos = True
    for d in diffs:
        if abs(d) < 1 or abs(d) > 3:
            could_be_safe = False
            break
        if d > 0:
            all_neg = False
        if d < 0:
            all_pos = False
    
    if (all_pos or all_neg) and could_be_safe:
        return True

for line in new_lines:
    if is_safe_report(line):
        safe_reports += 1
    else:
        sublists = [line[:i] + line[i+1:] for i in range(len(line))]
        for sublist in sublists:
            if is_safe_report(sublist):
                safe_reports += 1
                break



    

print(safe_reports)