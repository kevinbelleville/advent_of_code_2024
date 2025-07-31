import re

with open('input_day3.txt', 'r') as file:
    code = file.read()

# Advent of Code Day 3 Solution
# first I'll have to check to make sure the 'mul' exists
# then the '('
# three numbers are allowed, but less can be NO other chars
# a comma
# three nums, nothing else, but less is allowed,
# another ')' ends

def parse_code(code):
    pattern = r"mul\(\d{,3},\d{,3}\)|do\(\)|don\'t\(\)"
    matches = re.findall(pattern, code)
    return matches

list_of_matches = parse_code(code)

def process_matches(matches):
    sum = 0
    okay_to_process = True # starts True but will be False if hits a dont
    for match in matches:
        if match == "don't()":
            okay_to_process = False
            continue
        if match == "do()":
            okay_to_process = True
            continue
        if okay_to_process:
            nums = re.findall(r"\d+", match)
            if len(nums) == 2:
                result = int(nums[0]) * int(nums[1])
                sum += result
                print(f"Multiplying {nums[0]} and {nums[1]} gives {result}")
    return sum

results = process_matches(list_of_matches)

if __name__ == "__main__":
    print("Results of multiplications:", results)