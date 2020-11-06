def letter_to_number(word):
    sum = 0
    for Letter in word:
        sum += ord(Letter)
    sum -= 64 * len(word)
    return sum


with open('p022_names.txt', 'r') as file:
    raw_text = file.read().replace('\"', '')

name_list = raw_text.split(',')
name_list.sort()
tot = 0
for i in range(len(name_list)):
    tot += (i+1) * letter_to_number(name_list[i])
print(tot)