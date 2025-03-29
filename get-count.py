# Code Wars 7 kyu kata
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    vowel_count = 0
    vowels = ('a', 'e', 'i', 'o', 'u')
    for c in sentence:
        if c in vowels:
            vowel_count += 1
    return vowel_count

print(get_count('aeiou'))

# Test with a string containing all vowels
print(get_count('aeiou'))  # Expected output: 5

# Test with a string containing no vowels
print(get_count('bcdfg'))  # Expected output: 0

# Test with a string containing repeated vowels
print(get_count('aaeeiioouu'))  # Expected output: 10

# Test with a string containing vowels and consonants
print(get_count('hello world'))  # Expected output: 3

# Test with an empty string
print(get_count(''))  # Expected output: 0

# Test with a string containing spaces only
print(get_count('     '))  # Expected output: 0

# Test with a long string
print(get_count('the quick brown fox jumps over the lazy dog'))  # Expected output: 11