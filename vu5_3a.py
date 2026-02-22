# Returnerar ett heltal med antalet vokaler som finns i ordet
# (aeiouyåäö)
def count_vowels(word):
    vowels = "aeiouyåäö"
    count = 0

    for char in word.lower():
        if char in vowels:
            count += 1
    return count