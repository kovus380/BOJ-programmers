from collections import Counter

name = input()

counter = sorted(Counter(name).items())

last = ''
left = ''

for key, value in counter:
    if value % 2 == 0:
        left += key * (value//2)
    elif last:
        print("I'm Sorry Hansoo")
        exit()
    else:
        last = key
        left += key * (value//2)

print(left + last + left[::-1])