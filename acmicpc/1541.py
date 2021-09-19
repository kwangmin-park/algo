minus_splited_input = input().split('-')
total_val = 0

for first_val in minus_splited_input[0].split('+'):
    total_val += int(first_val)
for minus_splited_val in minus_splited_input[1:]:
    plus_splited_input = minus_splited_val.split('+')
    for plus_splited_val in plus_splited_input:
        total_val -= int(plus_splited_val)

print(total_val)