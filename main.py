word = input()
word_lower = word.lower()
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for letter in word_lower:
    if letter in vowels:
        count += 1

print(count)