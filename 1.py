def get_data() -> list[str]:
    with open("day-1-data.txt") as f:
        data_raw = f.readlines()
        data = [line.strip() for line in data_raw]
        return data

# Part 1 
#import re

#def run_part_1():
#    digits_re = re.compile("[0-9]")
#    total_sum_str = []
#    data = get_data()
#
#    for row in data:
#        match = re.findall(digits_re, row)
#        total_sum_str.append(match[0] + match[-1])
#    total_sum = sum(int(i) for i in total_sum_str)
#    print(total_sum)

# Part 2
import re

# Text to number mapping, excluding 'ten'
text_to_num = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

pattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))')

def extract_number(match: str) -> int:
        extracted_num = None
        if len(match) > 1:
            extracted_num = int(text_to_num[match])
        else:
            extracted_num = int(match)    
        return extracted_num

def sum_numbers(data: List[str]) -> int:
    total_sum = 0
    for row in data:
        matches = [match.group(1) for match in re.finditer(pattern, row)]
        first_digit, last_digit = extract_number(matches[0]), extract_number(matches[-1])
        total_sum += first_digit * 10 + last_digit
    return total_sum

def run_part_2():
    data = get_data()
    print(sum_numbers(data))

if __name__ == "__main__":
    #run_part_1()
    run_part_2()