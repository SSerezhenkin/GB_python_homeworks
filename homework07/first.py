def count_vowels(word):
    vowels = "аеёиоуыэюяaeiouy"
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count

poem = input("Введите стихотворение: ")
phrases = poem.split()

vowel_counts = []
for phrase in phrases:
    words = phrase.split("-")
    count = sum(count_vowels(word) for word in words)
    vowel_counts.append(count)

if len(set(vowel_counts)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")
